'''

Copyright 2019 Louis Ronald

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.



'''

from .common.datastructures import Data, TileGrid, DataGrid, Tile
from .writers.HTMLWriter import HTMLWriter
from .readers.CSVReader import CSVReader
import re

class ColorEx:



    def __init__(self, options=dict()):
        ''' Initialize a new engine '''

        self.default_rgb_code = ""
        self.filename = ""
        self.fileformat = ""

        
        self.default_rgb_code = self.get_hex_from_color('default')
        if(bool(options) is True):
            if('default-color' in options):
                if(self.is_rgb_hex(options['default-color'])):
                    self.default_rgb_code = options['default-color']
                elif(self.is_color_name(options['default-color'].lower())):
                     self.default_rgb_code = self.get_hex_from_color(
                         options['default-color'].lower())
                else:
                    self.default_rgb_code = self.get_hex_from_color('default')
            if('colors' in options):
                self.rgb_color_codes = options['colors']

            self.filename = options["source"][0]
            self.fileformat = options["source"][1]
            self.title = options["title"]
            self.subtitle = options["subtitle"]
            

    def get_rgb_color_names(self):
        colors = dict()
        colors['default'] = '#000000'
        colors['black'] = '#000000'
        colors['white'] = '#ffffff'
        colors['red'] = '#ff0000'
        colors['lime'] = '#00ff00'
        colors['blue'] = '#0000ff'
        colors['yellow'] = '#ffff00'
        colors['cyan'] = '#00ffff'
        colors['aqua'] = '#00ffff'
        colors['magenta'] = '#ff00ff'
        colors['fuchsia'] = '#ff00ff'
        colors['silver'] = '#c0c0c0'
        colors['gray'] = '#808080'
        colors['grey'] = '#808080'
        colors['maroon'] = '#800000'
        colors['olive'] = '#808000'
        colors['green'] = '#008000'
        colors['purple'] = '#800080'
        colors['teal'] = '#008080'
        colors['navy'] = '#000080'
        return colors



        

    def generate_tilegrid(self, data_grid):
        ''' creates an object of type TileGrid '''
        new_data = list()
        max_values = data_grid.calculate_max_values_by_cols()
        tilegrid = list()
        tilegrid.append(data_grid.grid[0])
        
        for row in data_grid.grid[1:]:
            final_row = list()
            rgb_index = 0
            for item in range(len(row)):
                if(type(row[item]) is Data):
                    try:
                        current_rgb = str()
                        if(self.is_rgb_hex(
                            self.rgb_color_codes[rgb_index])):
                           current_rgb = self.rgb_color_codes[rgb_index]
                        elif(self.is_color_name(
                            self.rgb_color_codes[rgb_index])):
                            current_rgb = self.get_hex_from_color(
                                self.rgb_color_codes[rgb_index])
                        else:
                            current_rgb = self.default_rgb_code
                    except:
                        current_rgb = self.default_rgb_code
                    new_tile = self.__generate_tile(row[item],
                        max_values[item], current_rgb)
                    final_row.append(new_tile)

                    rgb_index += 1
                else:
                    final_row.append(row[item])
            tilegrid.append(final_row)
            
        tilegrid_obj = TileGrid({'data': tilegrid, 'title': self.title,
                                 'subtitle': self.subtitle})
        return tilegrid_obj



        
        
    def __generate_tile(self, data_item, max_value, rgb):
        ''' generates a new tile of type Tile '''
        tile_options = {
                'value': data_item.value,
                'alpha': self.calculate_rgb_alpha(
                    data_item.value,
                    max_value),
                'rgb': self.rgb_hex_to_decimal(rgb)
        }
        return Tile(tile_options)




    

    def calculate_rgb_alpha(self, data_item, max_value):
        ''' calculates the alpha value for rgb color given
            data object and max value '''
        alpha_value = data_item / max_value
        return alpha_value





    def get_hex_from_color(self, color):
        ''' returns hex code given a color name '''
        colors = self.get_rgb_color_names()
        return colors[color]





    def is_rgb_hex(self, hex_code):
        ''' confirms whether or not a RGB hex code is valid '''
        if(hex_code[0] == '#' and len(hex_code) == 7):
            try:
                int(hex_code[1:],16)
                return True
            except:
                return False
        else:
            return False



    def rgb_hex_to_decimal(self, rgb_hex):
        if(rgb_hex[0]=='#'):
            rgb_hex = rgb_hex[1:]
        r = int(re.findall('..', str(rgb_hex))[0], base=16)
        g = int(re.findall('..', str(rgb_hex))[1], base=16)
        b = int(re.findall('..', str(rgb_hex))[2], base=16)
        return (r,g,b)



    def is_color_name(self, color_name):
        ''' confirms whether or not a color name is valid, based
        on internal color dictionary '''
        if(color_name in self.get_rgb_color_names()):
            return True
        else:
            return False




    def to_html(self, html_filename, template):
        ''' outputs TileGrid object to a HTML file '''
        if(self.fileformat.lower() == 'csv'):
            reader = CSVReader(self.filename)
            data_grid = reader.generate_datagrid()
            tile_grid = self.generate_tilegrid(data_grid)
            html_writer = HTMLWriter(html_filename, tile_grid)
            html_writer.write({'template': template})
        else:
            raise Exception





class MissingParametersError(Exception):
    pass

class InvalidParametersError(Exception):
    pass


