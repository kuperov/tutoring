import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
import numpy as np

# Set a style suitable for clean, white background with black elements
#plt.style.use('default')

def create_bar_chart(data, labels, title, filename, x_label, y_label):
    fig, ax = plt.subplots(figsize=(4, 3))
    bars = ax.bar(labels, data, width=0.6, fill=None)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(x_label, fontsize=9) # Set x-axis label
    ax.set_ylabel(y_label, fontsize=9) # Set y-axis label
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    patterns = ['//', '.', r'\\', '*', 'x', 'o', 'O', '+']
    for bar, pattern in zip(bars, patterns):
        bar.set_hatch(pattern)
    plt.tight_layout()
    plt.savefig(filename, format='pdf')
    plt.show()
    plt.close(fig)

def create_pie_chart(data, labels, title, filename):
    fig, ax = plt.subplots(figsize=(4, 3))
    # 'autopct' removed for no data annotations. Text color set to black.
    wedges, texts = ax.pie(data, labels=labels, startangle=90,
                           wedgeprops=dict(width=0.4, edgecolor='k'), colors=['white'])
    #wedgeprops={"edgecolor":"k",'linewidth': 5, 'linestyle': 'dashed', 'antialiased': True})
    ax.set_title(title, fontsize=10)
    ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

    patterns = ['//', '.', r'\\', '*', 'x', 'o', 'O', '+']
    for wedge, pattern in zip(wedges, patterns):
        wedge.set_hatch(pattern)

    # Adjust font sizes and ensure text color is black
    for text in texts:
        text.set_fontsize(8)
        text.set_color('black')

    plt.tight_layout()
    plt.savefig(filename, format='pdf')
    plt.show()
    plt.close(fig)

def create_line_chart(x_data, y_data, title, x_label, y_label, filename):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(x_data, y_data, marker='o', linestyle='-', color='black', linewidth=1)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(x_label, fontsize=9) # Set x-axis label
    ax.set_ylabel(y_label, fontsize=9) # Set y-axis label
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.grid(True, linestyle='--', alpha=0.7, color='grey') # Grid lines remain, but subtle
    plt.tight_layout()
    plt.savefig(filename, format='pdf')
    plt.show()
    plt.close(fig)

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
