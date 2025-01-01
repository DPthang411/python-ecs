class Entity:
    idCounter=0
    def __init__(self):
        self.id = Entity.idCounter
        Entity.idCounter+=1
class System:
    def __init__(self, requiredComponent):
        self.requiredSystem = requiredComponent
    def update(self, component):
        pass

class EntityManager:
    def __init__(self):
        self.entities = []
    def registerEntity(self, entity):
        if not (entity in self.entities):
            self.entities.append(entity)
    def unregisterEntity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
    def getEntityId(self, entity):
        return entity.id
class ComponentManager:
    def __init__(self):
        self.components = []
    def registerComponent(self, entity, component):
        if entity.id not in self.components:
            self.components[entity]=[]
        self.components[entity].append(component)
    def registerComponents(self,entity, *components):
        if entity.id not in self.components:
            self.components[entity.id]=[]
        for entity in components:
            for component in entity:
                self.components[entity.id].append(component)
                break
    def unregisterComponents(self, entity, componentType):
        for entity in self.components:
            for component in entity:
                if type(component) == componentType:
                    self.components[entity.id].remove(component)
                    break
    def getComponent(self, entity, componentType=None):
        if componentType ==None:
            return None
        else:
            for entity in self.components:
                for component in entity:
                    if componentType == type(component):
                        return component
    def getComponents(self, entity):
        return self.components.get(entity.id, [])
class SystemManager:
    def __init__(self, componentManager):
        self.systems = []
        self.componentManager = componentManager
    def registerSystem(self,entity, system):
        if entity.id not in self.systems:
            self.systems[entity.id]=[]
        for entity in self.systems:
            components = self.componentManager.getComponents(entity)
            if any(components)==system.requiredComponent:
                self.systems[entity.id].append(system)
            
    def unregisterSystem(self, entity, systemType):
        for entity in self.systems:
            for system in entity:
                if type(system) == systemType:
                    self.systems[entity.id].remove(system)
                    break
class World:
    def __init__(self):
        self.entityManager = EntityManager()
        self.componentManager = ComponentManager()
        self.systemManager = SystemManager(self.componentManager)
    def update(self):
        for entity in self.entityManager.entities:
            components = self.componentManager.getComponents(entity)
            for system in self.systemManager.systems.get(entity.id, []):
                system.update(components)
