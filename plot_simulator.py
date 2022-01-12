import setups
import matplotlib.pyplot as plt
import plot_sim_tools
import time
from matplotlib import patches
from blitting import BlitManager

# load setup
setup = setups.solar_system_inner

# set up  simulation parameters
system = setup['system']
window_size = setup['window_size']
x_range = setup['x_range']
y_range = setup['y_range']
dt = setup['dt']
wait = setup['wait']
name = setup['name']

# set up time tracking
elapsed_time = [0] * 5

# normalize colors so matplotlib can use the rgb values
for mass in system.masses:
    mass.normalize_color(norm=1)

# prepare plot data and artists
xdata = system.masses_x
ydata = system.masses_y
colors = [mass.color for mass in system.masses]

# setup static canvas
fig, ax = plt.subplots(figsize=(10, 10))
plt.axis([x_range[0], x_range[1], y_range[0], y_range[1]])
ax.set_title(name)
legend_handles = [patches.Patch(color=mass.color, label=mass.name) for mass in system.masses]
ax.legend(handles=legend_handles)
ax.text(0.99, 0.03, 'press q to exit'.format(*elapsed_time),
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)

# connect exit signal to pressing of 'q' during animation loop
cid = fig.canvas.mpl_connect("close_event", lambda event: exit(0))

# set up animated artists
scatter = ax.scatter(xdata, ydata, c=colors, animated=True)
time_tracker = ax.text(0.1, 0.9, 'elapsed time: {}y {}d {}h {}m {:.2f}s'.format(*elapsed_time),
                       horizontalalignment='left',
                       verticalalignment='bottom',
                       transform=ax.transAxes,
                       animated=True)

bm = BlitManager(fig.canvas, [scatter, time_tracker])

plt.show(block=False)
plt.pause(0.01)

while True:
    # update parameters
    system.update_velocities(dt)
    system.update_positions(dt)
    elapsed_time = plot_sim_tools.update_time(elapsed_time, dt)
    # update artists
    scatter.set_offsets([mass.position for mass in system.masses])
    time_tracker.set_text('elapsed time: {}y {}d {}h {}m {:.2f}s'.format(*elapsed_time))

    # update animation
    bm.update()
    time.sleep(0.01)
