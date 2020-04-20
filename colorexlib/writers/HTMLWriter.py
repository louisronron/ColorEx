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

from .FileOutputWriter import FileOutputWriter
from Cheetah.Template import Template
from ..common.exceptions import *

class HTMLWriter(FileOutputWriter):

    ''' Class that handles writing to HTML output files '''

    def __init__(self, filepath=None, heatmap=None, stylesheet=None):
        ''' Initialize HTMLWriter object '''
        if(filepath==None or heatmap==None or stylesheet==None):
            raise Exception

        
        super().__init__(filepath, heatmap, stylesheet)
        self.dirs = dict()

    def write(self, options):
        ''' write the HeatMap to output HTML file '''
        filepath = self.filepath
        output_file = open(filepath, "w")
        template_filename = options['template']
        template_file = open(template_filename, 'r')
        template_str = template_file.read()
        template = Template(template_str,
            searchList=[{'heatmap': self.heatmap.grid[1:],
                         'column_labels': self.heatmap.grid[0],
                         'title': self.heatmap.title,
                         'subtitle': self.heatmap.subtitle,
                         'theme': self.heatmap.theme,
                         'stylesheet': self.stylesheet}])
        output_file.write(str(template))
        output_file.close()
