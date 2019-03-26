
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = []
        segments = path.split("/")
        for segment in segments:
            path_stack.append(segment)
            if segment == "." or segment == '':
                path_stack.pop()
            elif segment == "..":
                if len(path_stack) > 1:
                    path_stack.pop()
                    path_stack.pop()
                else:
                    path_stack.pop()

        ans = "/".join(path_stack)
        if not ans.startswith("/"):
            ans = "/" + ans
        # print "ans:", ans
        return ans

if __name__=='__main__':
	print(Solution().simplifyPath('/a//./b/../../c/'))