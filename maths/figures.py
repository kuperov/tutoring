import matplotlib.pyplot as plt
import numpy as np


def draw_clock(hour, minute, second=0, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 4))
    else:
        fig = ax.get_figure()
    ax.set_aspect('equal', adjustable='box')

    # Draw the clock face
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    ax.add_artist(circle)

    # Draw hour markings and numbers
    for i in range(1, 13):
        angle_rad = np.deg2rad(90 - (i * 30))
        # Markings
        ax.plot([0.9 * np.cos(angle_rad), 1.0 * np.cos(angle_rad)],
                [0.9 * np.sin(angle_rad), 1.0 * np.sin(angle_rad)], color='black', linewidth=2)
        # Numbers - position slightly inside the outer circle
        text_angle_rad = np.deg2rad(90 - (i * 30))
        text_radius = 0.8
        ax.text(text_radius * np.cos(text_angle_rad), text_radius * np.sin(text_angle_rad),
                str(i), fontsize=12, ha='center', va='center', color='black')

    # Draw minute markings
    for i in range(60):
        angle_rad = np.deg2rad(90 - (i * 6))
        if i % 5 != 0:
             ax.plot([0.95 * np.cos(angle_rad), 1.0 * np.cos(angle_rad)],
                    [0.95 * np.sin(angle_rad), 1.0 * np.sin(angle_rad)], color='black', linewidth=1)


    # Draw the hour hand
    # Hour hand moves 360 degrees in 12 hours = 30 degrees per hour
    # Also moves based on minutes: 30 degrees per hour / 60 minutes = 0.5 degrees per minute
    hour_angle_rad = np.deg2rad(90 - ((hour % 12) + minute/60) * 30) # Use hour % 12 for 12-hour format
    ax.plot([0, 0.6 * np.cos(hour_angle_rad)], [0, 0.6 * np.sin(hour_angle_rad)], color='black', linewidth=4)

    # Draw the minute hand
    # Minute hand moves 360 degrees in 60 minutes = 6 degrees per minute
    minute_angle_rad = np.deg2rad(90 - minute * 6)
    ax.plot([0, 0.8 * np.cos(minute_angle_rad)], [0, 0.8 * np.sin(minute_angle_rad)], color='black', linewidth=3)

    # Draw the second hand (optional, but for completeness)
    # Second hand moves 360 degrees in 60 seconds = 6 degrees per second
    second_angle_rad = np.deg2rad(90 - second * 6)
    ax.plot([0, 0.7 * np.cos(second_angle_rad)], [0, 0.7 * np.sin(second_angle_rad)], color='gray', linewidth=0.5)

    # Center dot
    ax.plot(0, 0, 'o', color='black', markersize=5)

    # Set plot limits and remove axes
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_axis_off()

    return ax
