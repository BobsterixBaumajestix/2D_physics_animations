import cv2 as cv
import setups

# load setup
setup = setups.harmonic_oscillator_complex

# set up  simulation
system = setup['system']
window_size = setup['window_size']
x_range = setup['x_range']
y_range = setup['y_range']
dt = setup['dt']
wait = setup['wait']
name = setup['name']

years = 0
days = 0
hours = 0
minutes = 0
seconds = 0

italic = cv.FONT_ITALIC

while True:
    # display state
    out = system.visualize(imsize=window_size, x_range=x_range, y_range=y_range, rad_scale=1, rad_power=1)
    cv.putText(out, 'time elapsed: {}y {}d {}h {}m {:.2f}s'.format(years, days, hours, minutes, seconds),
               (50, 50), italic, 1, (0, 0, 0), thickness=2, lineType=cv.LINE_AA)
    cv.imshow(name, out)

    if cv.waitKey(1) == ord('q'):
        break

    # update state
    system.update_velocities(dt)
    system.update_positions(dt)
    # system.print_status()

    # update time
    seconds += dt
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60
    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60
    if hours >= 24:
        days += hours // 24
        hours = hours % 24
    if days >= 365:
        years += days // 365
        days = days % 365
