i#https://leetcode.com/problems/flood-fill/



class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if not image or not image[0]:
            return image
        n_rows = len(image)
        n_cols = len(image[0])
        current_color = image[sr][sc]
        if current_color == newColor:
            return image

        visited = set([])
        self.fill(sr, sc, image, current_color,  newColor, n_rows, n_cols, visited)
        return image

    def fill(self, curr_x, curr_y, image, current_color, color, n_rows, n_cols, visited):

        if (curr_x,curr_y) not in visited :
            visited.add((curr_x,curr_y))
            print(visited)
            if image[curr_x][curr_y] == current_color:
                image[curr_x][curr_y] = color
                if curr_x + 1 < n_rows:
                    self.fill(curr_x+1, curr_y, image, current_color,color, n_rows, n_cols, visited)
                if curr_y + 1 < n_cols:
                    self.fill(curr_x, curr_y+1, image, current_color,color, n_rows, n_cols, visited)
                if curr_x -1 >= 0:
                    self.fill(curr_x-1, curr_y, image, current_color, color, n_rows, n_cols, visited)
                if curr_y -1 >=0 :
                    self.fill(curr_x, curr_y-1, image, current_color, color, n_rows, n_cols, visited)
        return image
