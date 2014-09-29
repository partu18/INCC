import os

working_directory = os.getcwd()

#Images path's:
result_path = working_directory + '/../resultados/result.txt'
circle_image_path = working_directory+'/../imagenes/circle.png'
arrow_image_path = working_directory+'/../imagenes/arrow.png'
line_image_path = working_directory+'/../imagenes/line.png'


#Keys lists: 
RH_ARROWS_KEYLIST = ['right','left' ]
LH_ARROWS_KEYLIST = ['a','d']
RH_TAPPING_KEYLIST = ['return']
LH_TAPPING_KEYLIST = ['space']
NORM_DUAL_KEYLIST = ['space','left','right']
SPEC_DUAL_KEYLIST = ['return','a','d']
