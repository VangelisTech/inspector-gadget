import enum
from enum import auto
from typing import Dict, List, Optional


class FAIFPattern(enum.Enum):
    """
    Enumeration of Python design patterns from the FAIF (Foundations of AI Fairness) repository,
    organized by the repository's file structure.
    
    This enum provides a structured way to reference and categorize design patterns
    used in AI fairness implementations.
    """
    
    # Creational Patterns
    ABSTRACT_FACTORY = auto()
    BUILDER = auto()
    FACTORY_METHOD = auto()
    PROTOTYPE = auto()
    SINGLETON = auto()
    
    # Structural Patterns
    ADAPTER = auto()
    BRIDGE = auto()
    COMPOSITE = auto()
    DECORATOR = auto()
    FACADE = auto()
    FLYWEIGHT = auto()
    PROXY = auto()
    
    # Behavioral Patterns
    CHAIN_OF_RESPONSIBILITY = auto()
    COMMAND = auto()
    INTERPRETER = auto()
    ITERATOR = auto()
    MEDIATOR = auto()
    MEMENTO = auto()
    OBSERVER = auto()
    STATE = auto()
    STRATEGY = auto()
    TEMPLATE_METHOD = auto()
    VISITOR = auto()
    
    # Additional Patterns
    DEPENDENCY_INJECTION = auto()
    REPOSITORY = auto()
    UNIT_OF_WORK = auto()
    
    @classmethod
    def get_patterns_by_category(cls) -> Dict[str, List['FAIFPattern']]:
        """
        Returns patterns organized by their category.
        
        Returns:
            Dict mapping category names to lists of patterns in that category.
        """
        return {
            "Creational": [
                cls.ABSTRACT_FACTORY, cls.BUILDER, cls.FACTORY_METHOD,
                cls.PROTOTYPE, cls.SINGLETON
            ],
            "Structural": [
                cls.ADAPTER, cls.BRIDGE, cls.COMPOSITE, cls.DECORATOR,
                cls.FACADE, cls.FLYWEIGHT, cls.PROXY
            ],
            "Behavioral": [
                cls.CHAIN_OF_RESPONSIBILITY, cls.COMMAND, cls.INTERPRETER,
                cls.ITERATOR, cls.MEDIATOR, cls.MEMENTO, cls.OBSERVER,
                cls.STATE, cls.STRATEGY, cls.TEMPLATE_METHOD, cls.VISITOR
            ],
            "Additional": [
                cls.DEPENDENCY_INJECTION, cls.REPOSITORY, cls.UNIT_OF_WORK
            ]
        }
    
    @classmethod
    def get_pattern_description(cls, pattern: 'FAIFPattern') -> Optional[str]:
        """
        Returns a description of the specified pattern.
        
        Args:
            pattern: The pattern to describe
            
        Returns:
            A string description of the pattern or None if not found
        """
        descriptions = {
            cls.ABSTRACT_FACTORY: "Provides an interface for creating families of related objects without specifying concrete classes",
            cls.BUILDER: "Separates the construction of a complex object from its representation",
            cls.FACTORY_METHOD: "Defines an interface for creating an object, but lets subclasses decide which class to instantiate",
            cls.PROTOTYPE: "Creates new objects by copying an existing object",
            cls.SINGLETON: "Ensures a class has only one instance and provides a global point of access to it",
            
            cls.ADAPTER: "Converts the interface of a class into another interface clients expect",
            cls.BRIDGE: "Decouples an abstraction from its implementation so that the two can vary independently",
            cls.COMPOSITE: "Composes objects into tree structures to represent part-whole hierarchies",
            cls.DECORATOR: "Attaches additional responsibilities to an object dynamically",
            cls.FACADE: "Provides a unified interface to a set of interfaces in a subsystem",
            cls.FLYWEIGHT: "Uses sharing to support large numbers of fine-grained objects efficiently",
            cls.PROXY: "Provides a surrogate or placeholder for another object to control access to it",
            
            cls.CHAIN_OF_RESPONSIBILITY: "Passes a request along a chain of handlers until one handles it",
            cls.COMMAND: "Encapsulates a request as an object, allowing parameterization of clients with queuing, logging, etc.",
            cls.INTERPRETER: "Implements a specialized language by defining the grammar and interpreting sentences",
            cls.ITERATOR: "Provides a way to access elements of a collection sequentially without exposing its representation",
            cls.MEDIATOR: "Defines an object that encapsulates how a set of objects interact",
            cls.MEMENTO: "Captures and externalizes an object's internal state without violating encapsulation",
            cls.OBSERVER: "Defines a one-to-many dependency between objects so that when one changes state, all dependents are notified",
            cls.STATE: "Allows an object to alter its behavior when its internal state changes",
            cls.STRATEGY: "Defines a family of algorithms, encapsulates each one, and makes them interchangeable",
            cls.TEMPLATE_METHOD: "Defines the skeleton of an algorithm, deferring some steps to subclasses",
            cls.VISITOR: "Represents an operation to be performed on elements of an object structure",
            
            cls.DEPENDENCY_INJECTION: "A technique whereby one object supplies the dependencies of another object",
            cls.REPOSITORY: "Mediates between the domain and data mapping layers using a collection-like interface",
            cls.UNIT_OF_WORK: "Maintains a list of objects affected by a business transaction and coordinates changes"
        }
        return descriptions.get(pattern)
