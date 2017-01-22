from model.dt import RoadMap
from controller.viz import Viz
def main():
    mapA = RoadMap()
    viz = Viz(mapA)
    viz.show()

main()
