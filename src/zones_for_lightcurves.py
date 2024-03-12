import numpy as np
from tqdm import tqdm

from bokeh import events
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput, CustomJS, Whisker, BoxAnnotation, Div
from bokeh.plotting import figure


def plotter(the_lightcurve_, height_and_width_=(325, 900), high_mag_plotting_=False, starting_and_ending_days_1_=None,
            starting_and_ending_days_2_=None, starting_and_ending_days_3_=None):
    """
    The main plotter function with a few call backs (change title, change circle size, change circle alpha)
    :param the_lightcurve_: the lightcurve object, loaded with LightCurves class
    :param height_and_width_: height and width of the plot
    :param high_mag_plotting_: if high magnification intervals should be plotted
    :param starting_and_ending_days_1_: the starting and ending days of the first type of high magnification interval
    :param starting_and_ending_days_2_: the starting and ending days of the second type of high magnification interval
    :param starting_and_ending_days_3_: the starting and ending days of the third type of high magnification interval
    :return:
    """
    days, fluxes, cor_fluxes, fluxes_errors = the_lightcurve_.get_days_fluxes_errors()
    source = ColumnDataSource(data=dict(x=days, y=fluxes))
    # Set up plot
    height_, width_ = height_and_width_

    plot = figure(height=height_, width=width_, title=f'Lightcurve for {the_lightcurve_.lightcurve_name}')
    # x_range=[0, 4 * np.pi], y_range=[-2.5, 2.5])

    if high_mag_plotting_:
        plot = plotter_highlights(plot, starting_and_ending_days_1_, color=1.0)
        plot = plotter_highlights(plot, starting_and_ending_days_2_, color=2.0)
        plot = plotter_highlights(plot, starting_and_ending_days_3_, color=3.0)

    plot_controller = plot.circle('x', 'y', source=source, fill_alpha=0.7, size=5, legend_label='MOA-Red',
                                  color='brown')
    # plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    # Set up widgets
    text = TextInput(title="Title", value=f'Lightcurve for {the_lightcurve_.lightcurve_name}', width=300)
    circle_size = Slider(title="Circle Size (slow!)", value=5, start=0.01, end=10, step=0.01, width=250)
    circle_alpha = Slider(title="Circle Alpha", value=0.7, start=0.01, end=1, step=0.05, width=250)

    # Set up callbacks
    def update_title(attrname, old, new):
        plot.title.text = text.value

    text.on_change('value', update_title)

    callback_circle_size = CustomJS(args=dict(renderer=plot_controller), code="""
        renderer.glyph.radius = cb_obj.value;
    """)
    circle_size.js_on_change('value', callback_circle_size)
    # Circle Alpha
    callback_circle_alpha = CustomJS(args=dict(renderer=plot_controller), code="""
        renderer.glyph.fill_alpha = cb_obj.value;
        renderer.glyph.line_alpha = cb_obj.value;
    """)
    circle_alpha.js_on_change('value', callback_circle_alpha)

    # Set up layouts and add to document
    widget_inputs = row(text, circle_size, circle_alpha)
    return plot, widget_inputs


def plotter_with_errorbars(the_lightcurve_, main_plot_, high_mag_plotting_=False, starting_and_ending_days_1_=None,
                           starting_and_ending_days_2_=None, starting_and_ending_days_3_=None):
    """
    A secondary smaller plot that contains error bars and a few call backs
    (circle_size, circle_alpha, errorbar_line_width, errorbar_line_alpha)
    title changes with the main plot it is associated too
    :param the_lightcurve_: the lightcurve object, loaded with LightCurves class
    :param main_plot_: the main plot that this plot is associated with for zooming and moving axes purposes
    :param high_mag_plotting_: if high magnification intervals should be plotted
    :param starting_and_ending_days_1_: the starting and ending days of the first type of high magnification interval
    :param starting_and_ending_days_2_: the starting and ending days of the second type of high magnification interval
    :param starting_and_ending_days_3_: the starting and ending days of the third type of high magnification interval
    :return:
    """
    days, fluxes, cor_fluxes, fluxes_errors = the_lightcurve_.get_days_fluxes_errors()
    upper = [x + e for x, e in zip(fluxes, fluxes_errors)]
    lower = [x - e for x, e in zip(fluxes, fluxes_errors)]

    source = ColumnDataSource(data=dict(x=days, y=fluxes, yerr=fluxes_errors, upper=upper, lower=lower))
    # Set up plot
    plot = figure(height=275, width=600, title=main_plot_.title,
                  x_range=main_plot_.x_range, y_range=main_plot_.y_range)
    # tools="crosshair,pan,reset,save,wheel_zoom")

    if high_mag_plotting_:
        plot = plotter_highlights(plot, starting_and_ending_days_1_, color=1.0)
        plot = plotter_highlights(plot, starting_and_ending_days_2_, color=2.0)
        plot = plotter_highlights(plot, starting_and_ending_days_3_, color=3.0)

    plot_controller = plot.circle('x', 'y', source=source, fill_alpha=0.7, size=5, legend_label='MOA-Red',
                                  color='brown')

    whisker_errorbar = Whisker(source=source, base="x", upper="upper", lower="lower",
                               line_width=1.0, line_color='brown', line_alpha=1.0)  # level="overlay",
    whisker_errorbar.upper_head.line_color = 'brown'
    whisker_errorbar.lower_head.line_color = 'brown'
    plot.add_layout(whisker_errorbar)
    # plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    # Set up widgets
    circle_size = Slider(title="Circle Size", value=5, start=0.01, end=10, step=0.01, width=250)
    circle_alpha = Slider(title="Circle Alpha", value=0.7, start=0.1, end=1, step=0.05, width=250)
    errorbar_line_width = Slider(title="Error bar Width", value=1.0, start=0.5, end=3, step=0.1, width=250)
    errorbar_line_alpha = Slider(title="Error bar Alpha", value=1.0, start=0.1, end=1, step=0.05, width=250)

    # Set up callbacks
    # Circle Size
    callback_circle_size = CustomJS(args=dict(renderer=plot_controller), code="""
        renderer.glyph.radius = cb_obj.value;
    """)
    circle_size.js_on_change('value', callback_circle_size)

    # Circle Alpha
    callback_circle_alpha = CustomJS(args=dict(renderer=plot_controller), code="""
        renderer.glyph.fill_alpha = cb_obj.value;
        renderer.glyph.line_alpha = cb_obj.value;
    """)
    circle_alpha.js_on_change('value', callback_circle_alpha)

    # Error bar line width
    errorbar_line_width_callback = CustomJS(args=dict(renderer=whisker_errorbar), code="""
        renderer.line_width = cb_obj.value;
        renderer.upper_head.line_width = cb_obj.value;
        renderer.lower_head.line_width = cb_obj.value;
    """)
    errorbar_line_width.js_on_change('value', errorbar_line_width_callback)

    # Error bar line alpha
    errorbar_line_alpha_callback = CustomJS(args=dict(renderer=whisker_errorbar), code="""
        renderer.line_alpha = cb_obj.value;
        renderer.upper_head.line_alpha = cb_obj.value;
        renderer.lower_head.line_alpha = cb_obj.value;
    """)
    errorbar_line_alpha.js_on_change('value', errorbar_line_alpha_callback)

    # Set up layouts and add to document
    widget_inputs = row(column(circle_size, circle_alpha), column(errorbar_line_width, errorbar_line_alpha))
    return plot, widget_inputs


def highest_magnifications_finder(days_, fluxes_, times_standard_deviation_=1.0):
    """
    This function finds the days (every block of three points) with the high magnification points "High" is defined
    based on > median + standard deviation x times_standard_deviation_ (input)
    :param days_: the days of the
    lightcurve data points
    :param fluxes_: the fluxes of the lightcurve data points
    :param times_standard_deviation_:
    the number of times the standard deviation will be multiplied to be used as a threshold
    :return:
    """
    # Find the regions with the highest magnification points
    fluxes_ = fluxes_ - min(fluxes_)
    median_plus_std_flux = np.median(fluxes_) + times_standard_deviation_ * np.std(fluxes_)
    days_with_highest_magnification = []
    fluxes_in_highest_magnification_regions = []
    indexes_of_highest_magnification_regions = []
    for index_for_flux in tqdm(range(len(fluxes_) - 1)):
        if index_for_flux + 1 < (len(fluxes_) - 1):
            if fluxes_[index_for_flux] + fluxes_[index_for_flux + 1] + fluxes_[index_for_flux + 2] > median_plus_std_flux * 3:
                days_with_highest_magnification.append(days_[index_for_flux])
                fluxes_in_highest_magnification_regions.append(fluxes_[index_for_flux])
                indexes_of_highest_magnification_regions.append(index_for_flux)
        elif index_for_flux < (len(fluxes_) - 1):
            if fluxes_[index_for_flux] + fluxes_[index_for_flux + 1] > median_plus_std_flux * 2:
                days_with_highest_magnification.append(days_[index_for_flux])
                fluxes_in_highest_magnification_regions.append(fluxes_[index_for_flux])
                indexes_of_highest_magnification_regions.append(index_for_flux)
        elif index_for_flux == (len(fluxes_) - 1):
            if fluxes_[index_for_flux] > median_plus_std_flux:
                days_with_highest_magnification.append(days_[index_for_flux])
                fluxes_in_highest_magnification_regions.append(fluxes_[index_for_flux])
                indexes_of_highest_magnification_regions.append(index_for_flux)
        else:
            raise ValueError('Something went wrong with the highest magnification finder')
    return days_with_highest_magnification, fluxes_in_highest_magnification_regions, indexes_of_highest_magnification_regions


def hightest_interval_finder(days_, fluxes_, times_standard_deviation_=1.0):
    """
    This function finds the intervals with the highest magnification points.
    It calls the function highest_magnifications_finder
    :param days_: the days of the lightcurve data points
    :param fluxes_: the fluxes of the lightcurve data points
    :param times_standard_deviation_:
    the number of times the standard deviation will be multiplied to be used as a threshold
    :return:
    """
    days_with_highest_magnification, _, index_for_flux = highest_magnifications_finder(days_, fluxes_,
                                                                                       times_standard_deviation_)
    starting_and_ending_indexes = []
    starting_and_ending_days = []
    if index_for_flux.__len__() != 0:
        start_index = index_for_flux[0]
        end_index = index_for_flux[0]

        for choosing_index in tqdm(range(1, len(index_for_flux))):

            if index_for_flux[choosing_index] == end_index + 1:
                end_index = index_for_flux[choosing_index]
            else:
                starting_and_ending_indexes.append((start_index, end_index))
                starting_and_ending_days.append((days_[start_index], days_[end_index]))
                start_index = index_for_flux[choosing_index]
                end_index = index_for_flux[choosing_index]

        starting_and_ending_indexes.append((start_index, end_index))
        starting_and_ending_days.append((days_[start_index], days_[end_index]))
        return starting_and_ending_days, starting_and_ending_indexes
    else:
        print('No high magnification points found for cut3')
        return [(np.NaN, np.NaN)], [(np.NaN, np.NaN)]


def three_highest_intervals_finder(days_, fluxes_,
                                   times_standard_deviation_1_ = 1.0,
                                   times_standard_deviation_2_ = 2.0,
                                   times_standard_deviation_3_ = 3.0):
    """
    :param days_: the days of the lightcurve data points
    :param fluxes_: the fluxes of the lightcurve data points
    :param times_standard_deviation_1_: first number of times the standard deviation will be multiplied
    to be used as a threshold
    :param times_standard_deviation_2_: second number of times the standard deviation will be multiplied
    to be used as a threshold
    :param times_standard_deviation_3_: third number of times the standard deviation will be multiplied
    to be used as a threshold
    :return:
    """
    starting_and_ending_days_1, starting_and_ending_indexes_1 = hightest_interval_finder(days_, fluxes_,
                                                                                         times_standard_deviation_=times_standard_deviation_1_)
    starting_and_ending_days_2, starting_and_ending_indexes_2 = hightest_interval_finder(days_, fluxes_,
                                                                                         times_standard_deviation_=times_standard_deviation_2_)
    starting_and_ending_days_3, starting_and_ending_indexes_3 = hightest_interval_finder(days_, fluxes_,
                                                                                         times_standard_deviation_=times_standard_deviation_3_)
    return starting_and_ending_days_1, starting_and_ending_days_2, starting_and_ending_days_3


def plotter_highlights(plot_, starting_and_ending_, color=1.0):
    """
    This function plots the highlights in the plot.
    So far only three colors are available, for (median + (standard deviation x 1.0, 2.0 or 3.0))
    :param plot_:
    :param starting_and_ending_:
    :param color:
    :return:
    """
    # background_color #F3F7C1 Median + Stdv;
    # #D0EBC5: Median + 2Stdv;
    # #A8DBE3 Median + 3Stdv")
    for starting, ending in starting_and_ending_:
        if starting == ending:
            pass
        else:
            if color == 1.0:
                fill_color_ = '#F3F7C1'
            elif color == 2.0:
                fill_color_ = '#D0EBC5'
            elif color == 3.0:
                fill_color_ = '#A8DBE3'
            low_box = BoxAnnotation(left=starting, right=ending, fill_color=fill_color_, fill_alpha=1.0,
                                    line_alpha=1.0, line_color=fill_color_, level="underlay")
            plot_.add_layout(low_box)
    return plot_


def general_zones(the_lightcurve_, three_starting_and_ending_days_):
    """
    This function plots all the light curves zones for further analysis.
    We can control the big zone (with main plot to be doubled tapped on,
    and the following plot zones to be used for investigation)
    :param the_lightcurve_:
    :param three_starting_and_ending_days_: list of lists with the starting and ending days for the three zones
    :return:
    """
    big_plot, big_widgets_inputs = plotter(the_lightcurve_, height_and_width_=(370, 1200),
                                           high_mag_plotting_=True,
                                           starting_and_ending_days_1_=three_starting_and_ending_days_[0],
                                           starting_and_ending_days_2_=three_starting_and_ending_days_[1],
                                           starting_and_ending_days_3_=three_starting_and_ending_days_[2])

    # Here is the display configuration for the double click tool
    def display_event(div, attributes=[], style='float:left;clear:left;font_size=13px'):
        # Build a suitable CustomJS to display the current event in the div model.
        return CustomJS(args=dict(div=div), code="""
            const attrs = %s;
            const args = [];
            for (let i = 0; i<attrs.length; i++) {
                args.push(attrs[i] + '=' + Number(cb_obj[attrs[i]]).toFixed(2));
            }
            const line = "<span style=%r><b>" + cb_obj.event_name + "</b>(" + args.join(", ") + ")</span>\\n";
            const text = div.text.concat(line);
            const lines = text.split("\\n")
            if (lines.length > 35)
                lines.shift();
            div.text = lines.join("\\n");
        """ % (attributes, style))

    div = Div(width=400, height=big_plot.height, height_policy="fixed")
    # big_plot.js_on_event(events.DoubleTap, display_event(div, attributes=['x', 'y', 'sx', 'sy']))
    big_plot.js_on_event(events.DoubleTap, display_event(div, attributes=['x', 'y']))

    # Create main investigation plots
    # Block 1 of plots
    main_plot_1, main_widgets_inputs_1 = plotter(the_lightcurve_,
                                                 high_mag_plotting_=True,
                                                 starting_and_ending_days_1_=three_starting_and_ending_days_[0],
                                                 starting_and_ending_days_2_=three_starting_and_ending_days_[1],
                                                 starting_and_ending_days_3_=three_starting_and_ending_days_[2]
                                                 )
    secondary_plot_1, secondary_widgets_inputs_1 = plotter_with_errorbars(the_lightcurve_, main_plot_1,
                                                                          high_mag_plotting_=True,
                                                                          starting_and_ending_days_1_=
                                                                          three_starting_and_ending_days_[0],
                                                                          starting_and_ending_days_2_=
                                                                          three_starting_and_ending_days_[1],
                                                                          starting_and_ending_days_3_=
                                                                          three_starting_and_ending_days_[2]
                                                                          )
    # Block 2 of plots
    main_plot_2, main_widgets_inputs_2 = plotter(the_lightcurve_,
                                                 high_mag_plotting_=True,
                                                 starting_and_ending_days_1_=three_starting_and_ending_days_[0],
                                                 starting_and_ending_days_2_=three_starting_and_ending_days_[1],
                                                 starting_and_ending_days_3_=three_starting_and_ending_days_[2]
                                                 )
    secondary_plot_2, secondary_widgets_inputs_2 = plotter_with_errorbars(the_lightcurve_, main_plot_2,
                                                                          high_mag_plotting_=True,
                                                                          starting_and_ending_days_1_=
                                                                          three_starting_and_ending_days_[0],
                                                                          starting_and_ending_days_2_=
                                                                          three_starting_and_ending_days_[1],
                                                                          starting_and_ending_days_3_=
                                                                          three_starting_and_ending_days_[2]
                                                                          )
    # Block 3 of plots
    main_plot_3, main_widgets_inputs_3 = plotter(the_lightcurve_,
                                                 high_mag_plotting_=True,
                                                 starting_and_ending_days_1_=three_starting_and_ending_days_[0],
                                                 starting_and_ending_days_2_=three_starting_and_ending_days_[1],
                                                 starting_and_ending_days_3_=three_starting_and_ending_days_[2]
                                                 )
    secondary_plot_3, secondary_widgets_inputs_3 = plotter_with_errorbars(the_lightcurve_, main_plot_3,
                                                                          high_mag_plotting_=True,
                                                                          starting_and_ending_days_1_=
                                                                          three_starting_and_ending_days_[0],
                                                                          starting_and_ending_days_2_=
                                                                          three_starting_and_ending_days_[1],
                                                                          starting_and_ending_days_3_=
                                                                          three_starting_and_ending_days_[2]
                                                                          )

    main_plots = [main_plot_1, main_plot_2, main_plot_3]

    # Define a callback function to handle the DoubleTap event with a counter and update the X and Y axes ranges
    def double_tap_callback():
        return CustomJS(args=dict(main_plots=main_plots), code="""
            // Define the counter variable OR updated +1
            if (typeof window.doubletap_counter === 'undefined') {
            window.doubletap_counter = 0
            } else {
            window.doubletap_counter = window.doubletap_counter + 1
            }
            
            // Get the current data range of the x and y axes of the plot to update
            let current_plot = main_plots[window.doubletap_counter % main_plots.length];
            let x_range = current_plot.x_range;
            let y_range = current_plot.y_range;

            // Get the x-coordinate of the double-tap event
            let tap_x = cb_obj.x;
            let tap_y = cb_obj.y;

            // Calculate the new x-axis range
            let new_start_x = Math.max(0, tap_x - 100);
            let new_end_x = tap_x + 100;

            // Calculate the new y-axis range
            let new_start_y = tap_y - 20000;
            let new_end_y = tap_y + 20000;

            // Update the x-axis range
            x_range.setv({start: new_start_x, end: new_end_x});

            // Update the y-axis range
            y_range.setv({start: new_start_y, end: new_end_y});
        """)

    # Attach the DoubleTap event and the callback to the "big_plot"
    big_plot.js_on_event(events.DoubleTap, double_tap_callback())

    big_zone_layout_ = row(column(big_plot, big_widgets_inputs), div, width=1400)
    small_zone_layout_1_ = row(column(main_plot_1, main_widgets_inputs_1),
                               column(secondary_plot_1, secondary_widgets_inputs_1),
                               width=1200)
    small_zone_layout_2_ = row(column(main_plot_2, main_widgets_inputs_2),
                               column(secondary_plot_2, secondary_widgets_inputs_2),
                               width=1200)
    small_zone_layout_3_ = row(column(main_plot_3, main_widgets_inputs_3),
                               column(secondary_plot_3, secondary_widgets_inputs_3),
                               width=1200)
    return big_zone_layout_, small_zone_layout_1_, small_zone_layout_2_, small_zone_layout_3_
