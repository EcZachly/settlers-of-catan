from resource import Resource


class FixedImprovement:
    def __init__(self, required_resources: list[Resource]):
        self.required_resources = required_resources

    def place_improvement(self, tile_point):
        raise NotImplementedError("don't know how to place improvements yet")

    def get_required_cards(self):
        return self.required_resources

Settlement = FixedImprovement(required_resources=[Resource.SHEEP, Resource.BRICK, Resource.LUMBER, Resource.GRAIN])
City = FixedImprovement(required_resources=[Resource.ORE, Resource.ORE, Resource.ORE, Resource.GRAIN, Resource.GRAIN])
