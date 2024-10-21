#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import numpy as np; import math
import sip



class QAM64(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "QAM64")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.e_band = e_band = 1
        self.volt = volt = 0
        self.samp_rate = samp_rate = 32000
        self.samp_per_sym = samp_per_sym = 8
        self.excess_bw = excess_bw = e_band
        self.carrier_freq = carrier_freq = 1000000
        self.atten = atten = 1

        ##################################################
        # Blocks
        ##################################################

        self._volt_range = qtgui.Range(0, 20, .1, 0, 200)
        self._volt_win = qtgui.RangeWidget(self._volt_range, self.set_volt, "Channel Voltage", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._volt_win)
        self._atten_range = qtgui.Range(0, 1, .001, 1, 200)
        self._atten_win = qtgui.RangeWidget(self._atten_range, self.set_atten, "Attenuation", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._atten_win)
        self.root_raised_cosine_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                1,
                samp_rate,
                (samp_rate/samp_per_sym),
                excess_bw,
                (10*samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                1,
                samp_rate,
                (samp_rate/samp_per_sym),
                excess_bw,
                (10*samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                samp_per_sym,
                samp_rate,
                (samp_rate/samp_per_sym),
                excess_bw,
                (10*samp_per_sym+1)))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                samp_per_sym,
                samp_rate,
                (samp_rate/samp_per_sym),
                excess_bw,
                (10*samp_per_sym+1)))
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_f(
            1024, #size
            samp_rate, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(1)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(samp_per_sym)
        self.qtgui_eye_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(True)
        self.qtgui_eye_sink_x_0.enable_grid(False)
        self.qtgui_eye_sink_x_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0.enable_control_panel(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_eye_sink_x_0.set_line_label(i, "Eye[Data {0}]".format(i))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_eye_sink_x_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            10000, #size
            'Transition Diagram', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [-1, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            100, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(samp_per_sym, (np.hstack((1,np.zeros(samp_per_sym-1)))))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(samp_per_sym, (np.hstack((1,np.zeros(samp_per_sym-1)))))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self._e_band_range = qtgui.Range(0, 2, .01, 1, 200)
        self._e_band_win = qtgui.RangeWidget(self._e_band_range, self.set_e_band, "Excess Bandwidth", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._e_band_win)
        self.digital_map_bb_0_0 = digital.map_bb((1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4,1,2,3,4,-1,-2,-3,-4))
        self.digital_map_bb_0 = digital.map_bb((1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4, -1,-1,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4))
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_float*1, 1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_float*1, 1)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(6)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(atten)
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, samp_per_sym)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, samp_per_sym)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, (-carrier_freq), 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, carrier_freq, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 256, 1000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_UNIFORM, volt, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.root_raised_cosine_filter_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1, 0), (self.blocks_skiphead_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QAM64")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_e_band(self):
        return self.e_band

    def set_e_band(self, e_band):
        self.e_band = e_band
        self.set_excess_bw(self.e_band)

    def get_volt(self):
        return self.volt

    def set_volt(self, volt):
        self.volt = volt
        self.analog_noise_source_x_0.set_amplitude(self.volt)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_eye_sink_x_0.set_samp_rate(self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_sym, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(self.samp_per_sym, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.blocks_keep_one_in_n_0.set_n(self.samp_per_sym)
        self.blocks_keep_one_in_n_0_0.set_n(self.samp_per_sym)
        self.interp_fir_filter_xxx_0.set_taps((np.hstack((1,np.zeros(self.samp_per_sym-1)))))
        self.interp_fir_filter_xxx_0_0.set_taps((np.hstack((1,np.zeros(self.samp_per_sym-1)))))
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(self.samp_per_sym)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_sym, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(self.samp_per_sym, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_sym, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(self.samp_per_sym, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(1, self.samp_rate, (self.samp_rate/self.samp_per_sym), self.excess_bw, (10*self.samp_per_sym+1)))

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_0.set_frequency(self.carrier_freq)
        self.analog_sig_source_x_0_1.set_frequency((-self.carrier_freq))

    def get_atten(self):
        return self.atten

    def set_atten(self, atten):
        self.atten = atten
        self.blocks_multiply_const_vxx_0.set_k(self.atten)




def main(top_block_cls=QAM64, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
