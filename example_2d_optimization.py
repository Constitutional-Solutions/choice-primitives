#!/usr/bin/env python3
"""Example: 2D Position Optimization with Choice Primitives.

This script demonstrates how to use the choice primitives library
to find an optimal 2D position under constraints.
"""

import logging
from choice_primitives import Choice, ConstraintSet, UtilityFunctions

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Run 2D position optimization example."""
    
    logger.info("Starting 2D Position Optimization Example")
    logger.info("="*50)
    
    # Define candidate positions in 2D space
    positions = [
        (0, 0),
        (1, 1),
        (2, 3),
        (5, 5),
        (8, 2),
        (10, 10),
        (15, 1),
        (-2, 3),
        (12, 8),
        (6, 9)
    ]
    
    logger.info(f"Candidate positions: {len(positions)} points")
    for i, pos in enumerate(positions, 1):
        logger.info(f"  {i}. {pos}")
    
    # Create a Choice with these positions
    choice = Choice(positions)
    logger.info(f"\nInitialized {choice}")
    
    # Define constraints: stay within bounding box [0, 10] x [0, 10]
    logger.info("\nApplying constraints:")
    logger.info("  - Bounding box: x ∈ [0, 10], y ∈ [0, 10]")
    
    constraints = ConstraintSet()
    constraints.add(ConstraintSet.bounding_box(0, 10, 0, 10))
    
    # Filter choices based on constraints
    filtered_choice = choice.filter(constraints.check)
    logger.info(f"\nAfter filtering: {filtered_choice}")
    
    if filtered_choice.options:
        logger.info("Valid positions after filtering:")
        for i, pos in enumerate(filtered_choice.options, 1):
            logger.info(f"  {i}. {pos}")
    
    # Define utility function: maximize distance from origin
    logger.info("\nUtility function: Maximize distance from origin (0, 0)")
    
    # Calculate utility for each valid option
    logger.info("\nCalculating utilities:")
    for pos in filtered_choice.options:
        utility = UtilityFunctions.distance_from_origin(pos)
        logger.info(f"  Position {pos}: distance = {utility:.2f}")
    
    # Find optimal position
    optimal_position = filtered_choice.optimize(UtilityFunctions.distance_from_origin)
    optimal_distance = UtilityFunctions.distance_from_origin(optimal_position)
    
    # Print results
    logger.info("\n" + "="*50)
    logger.info("RESULT")
    logger.info("="*50)
    logger.info(f"Optimal position: {optimal_position}")
    logger.info(f"Distance from origin: {optimal_distance:.2f}")
    logger.info("\nExplanation:")
    logger.info(f"  Among all valid positions within the bounding box,")
    logger.info(f"  {optimal_position} is farthest from the origin.")
    
    # Also demonstrate minimization (closest to origin)
    logger.info("\n" + "="*50)
    logger.info("BONUS: Minimization Example")
    logger.info("="*50)
    logger.info("Utility function: Minimize distance from origin")
    
    closest_position = filtered_choice.optimize(UtilityFunctions.negative_distance_from_origin)
    closest_distance = UtilityFunctions.distance_from_origin(closest_position)
    
    logger.info(f"Closest position to origin: {closest_position}")
    logger.info(f"Distance from origin: {closest_distance:.2f}")
    
    logger.info("\n" + "="*50)
    logger.info("Example completed successfully!")
    logger.info("="*50)


if __name__ == "__main__":
    main()
