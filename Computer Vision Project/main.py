import Solver
import Face
import Cube
# for testing - 1 is white, 2 is orange, 3 is green, 4 is red, 5 is blue, 6 is yellow
# the bottom face (dface) is the one that gets solved first
uface = Face.face([[4,3,2],[1,6,4],[1,4,2]])
lface = Face.face([[6,2,5],[6,4,5],[2,4,6]])
fface = Face.face([[2,1,5],[2,3,1],[4,3,1]])
rface = Face.face([[6,5,6],[5,2,3],[5,2,4]])
bface = Face.face([[3,4,3],[1,5,5],[3,2,3]])
dface = Face.face([[5,6,4],[6,1,3],[1,6,1]])

mycube = Cube.cube(uface,lface,fface,rface,bface,dface,"")
mysolver = Solver.solver(mycube)
mysolver.solve()
mycube.show_cube()
