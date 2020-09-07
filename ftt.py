input_array = 100,100,100,-100,-100,-100,100,100,100,-100,-100,-100,100,100,100
class d_f_T:
    dft_dict = {}
    dft_dict['frequency_var'] = []
    dft_dict['amplitude_var'] = []
    dft_dict['phase_var'] = []
    dft_dict['coord_var'] = []
    x_real = 0
    y_imag = 0
    def discrete_fourrier_transform(self, input_array):
        self.range_var = len(input_array)
        for k in range(self.range_var):  
            for n in range(self.range_var):
                angle_var = (((2*np.pi)*k*n)/self.range_var)
                self.x_real += ((input_array[n])* np.cos(angle_var))
                self.y_imag += (-(input_array[n])* np.sin(angle_var))
            self.x_real = self.x_real / self.range_var
            self.y_imag = self.y_imag / self.range_var
            self.dft_dict['frequency_var'] += [k]
            self.dft_dict['amplitude_var'] += [((self.x_real**2)+(self.y_imag**2))**(1/2)]
            self.dft_dict['phase_var'] += [np.arctan2(self.y_imag, self.x_real)]
            self.dft_dict['coord_var'] += [(self.x_real,self.y_imag)]
        print(self.dft_dict)
call_dft = d_f_T()
call_dft.discrete_fourrier_transform(input_array)