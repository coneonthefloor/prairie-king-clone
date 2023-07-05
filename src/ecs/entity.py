class Entity:
    def __init__(self, name):
        self.name = name
        self.components = {}

    def update(self, events, delta_time):
        self.update_components(events, delta_time)

    def add_component(self, component):
        self.components[component.name] = component

    def get_component(self, component_name):
        return self.components[component_name]

    def update_components(self, events, delta_time):
        for _, component in enumerate(self.components):
            self.get_component(component).update(events, delta_time)
