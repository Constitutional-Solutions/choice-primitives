"""Choice Primitives - Core module for 2D decision elements.

This module provides classes for representing choices, constraints,
and utility functions in 2D space.
"""

import math
from typing import Tuple, List, Callable


class Choice:
    """Represents a choice with 2D position options."""
    
    def __init__(self, options: List[Tuple[float, float]]):
        """
        Initialize a Choice with a list of 2D position options.
        
        Args:
            options: List of (x, y) tuples representing possible positions
        """
        self.options = options
    
    def filter(self, constraint: Callable[[Tuple[float, float]], bool]) -> 'Choice':
        """
        Filter options based on a constraint function.
        
        Args:
            constraint: Function that returns True if option is valid
            
        Returns:
            New Choice with filtered options
        """
        filtered = [opt for opt in self.options if constraint(opt)]
        return Choice(filtered)
    
    def optimize(self, utility: Callable[[Tuple[float, float]], float]) -> Tuple[float, float]:
        """
        Select the option that maximizes the utility function.
        
        Args:
            utility: Function that returns a utility score for each option
            
        Returns:
            The optimal (x, y) position
        """
        if not self.options:
            raise ValueError("No valid options available")
        
        return max(self.options, key=utility)
    
    def __repr__(self):
        return f"Choice({len(self.options)} options)"


class ConstraintSet:
    """Collection of constraint functions for 2D positions."""
    
    def __init__(self):
        self.constraints = []
    
    def add(self, constraint: Callable[[Tuple[float, float]], bool]) -> 'ConstraintSet':
        """
        Add a constraint to the set.
        
        Args:
            constraint: Function that returns True if position is valid
            
        Returns:
            Self for method chaining
        """
        self.constraints.append(constraint)
        return self
    
    def check(self, position: Tuple[float, float]) -> bool:
        """
        Check if a position satisfies all constraints.
        
        Args:
            position: (x, y) tuple to check
            
        Returns:
            True if all constraints are satisfied
        """
        return all(constraint(position) for constraint in self.constraints)
    
    @staticmethod
    def bounding_box(x_min: float, x_max: float, y_min: float, y_max: float) -> Callable:
        """
        Create a bounding box constraint.
        
        Args:
            x_min, x_max: X-axis bounds
            y_min, y_max: Y-axis bounds
            
        Returns:
            Constraint function
        """
        def constraint(pos: Tuple[float, float]) -> bool:
            x, y = pos
            return x_min <= x <= x_max and y_min <= y <= y_max
        return constraint


class UtilityFunctions:
    """Collection of common utility functions for 2D positions."""
    
    @staticmethod
    def distance_from_origin(position: Tuple[float, float]) -> float:
        """
        Calculate Euclidean distance from origin (0, 0).
        
        Args:
            position: (x, y) tuple
            
        Returns:
            Distance from origin
        """
        x, y = position
        return math.sqrt(x**2 + y**2)
    
    @staticmethod
    def distance_from_point(target: Tuple[float, float]) -> Callable:
        """
        Create a utility function for distance from a specific point.
        
        Args:
            target: Target (x, y) position
            
        Returns:
            Utility function
        """
        def utility(position: Tuple[float, float]) -> float:
            x1, y1 = position
            x2, y2 = target
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return utility
    
    @staticmethod
    def negative_distance_from_origin(position: Tuple[float, float]) -> float:
        """
        Negative distance from origin (for minimization problems).
        
        Args:
            position: (x, y) tuple
            
        Returns:
            Negative distance from origin
        """
        return -UtilityFunctions.distance_from_origin(position)
"""
