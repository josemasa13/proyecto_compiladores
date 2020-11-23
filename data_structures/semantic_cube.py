from collections import defaultdict

semantic_cube = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: None)))


#Mathematical operators
semantic_cube['int']['int']['+']       = 'int'
semantic_cube['int']['int']['-']       = 'int'
semantic_cube['int']['int']['*']       = 'int'
semantic_cube['int']['int']['/']       = 'float'


semantic_cube['float']['float']['*']   = 'float'
semantic_cube['float']['float']['/']   = 'float'
semantic_cube['float']['float']['-']   = 'float'
semantic_cube['float']['float']['+']   = 'float'

semantic_cube['char']['char']['*']     = 'Error'
semantic_cube['char']['char']['/']     = 'Error'
semantic_cube['char']['char']['-']     = 'Error'
semantic_cube['char']['char']['+']     = 'Error'


semantic_cube['int']['float']['+'] = semantic_cube['float']['int']['+'] = 'float'
semantic_cube['int']['float']['-'] = semantic_cube['float']['int']['-'] = 'float'
semantic_cube['int']['float']['*'] = semantic_cube['float']['int']['*'] = 'float'
semantic_cube['int']['float']['/'] = semantic_cube['float']['int']['/'] = 'float'

semantic_cube['char']['int']['+'] = semantic_cube['int']['char']['+']         = 'Error'
semantic_cube['char']['float']['+'] = semantic_cube['float']['char']['+']     = 'Error'
semantic_cube['char']['int']['-'] = semantic_cube['int']['char']['-']         = 'Error'
semantic_cube['char']['float']['-'] = semantic_cube['float']['char']['-']     = 'Error'
semantic_cube['char']['int']['*'] = semantic_cube['int']['char']['*']         = 'Error'
semantic_cube['char']['float']['*'] = semantic_cube['float']['char']['*']     = 'Error'
semantic_cube['char']['int']['/'] = semantic_cube['int']['char']['/']         = 'Error'
semantic_cube['char']['float']['/'] = semantic_cube['float']['char']['/']     = 'Error'

semantic_cube['int']['int_arr']['*'] = semantic_cube['int_arr']['int']['*']  = 'Error'
semantic_cube['int']['int_arr']['/'] = semantic_cube['int_arr']['int']['/']  = 'Error'
semantic_cube['int']['int_arr']['+'] = semantic_cube['int_arr']['int']['+']  = 'Error'
semantic_cube['int']['int_arr']['-'] = semantic_cube['int_arr']['int']['-']  = 'Error'

semantic_cube['char']['int_arr']['*'] = semantic_cube['int_arr']['char']['*']  = 'Error'
semantic_cube['char']['int_arr']['/'] = semantic_cube['int_arr']['char']['/']  = 'Error'
semantic_cube['char']['int_arr']['+'] = semantic_cube['int_arr']['char']['+']  = 'Error'
semantic_cube['char']['int_arr']['-'] = semantic_cube['int_arr']['char']['-']  = 'Error'

semantic_cube['float']['int_arr']['*'] = semantic_cube['int_arr']['float']['*']  = 'Error'
semantic_cube['float']['int_arr']['/'] = semantic_cube['int_arr']['float']['/']  = 'Error'
semantic_cube['float']['int_arr']['+'] = semantic_cube['int_arr']['float']['+']  = 'Error'
semantic_cube['float']['int_arr']['-'] = semantic_cube['int_arr']['float']['-']  = 'Error'

semantic_cube['int_arr']['int_arr']['/'] = semantic_cube['int_arr']['int_arr']['/']  = 'Error'



#Comparative operators

semantic_cube['int']['int']['=']   = 'int'
semantic_cube['int']['int']['>']   = 'bool'
semantic_cube['int']['int']['<']   = 'bool'
semantic_cube['int']['int']['<=']  = 'bool'
semantic_cube['int']['int']['>=']  = 'bool'
semantic_cube['int']['int']['!=']  = 'bool'
semantic_cube['int']['int']['==']  = 'bool'
semantic_cube['bool']['bool']['|']  = 'bool'
semantic_cube['bool']['bool']['&']  = 'bool'

semantic_cube['float']['float']['=']   = 'float'
semantic_cube['float']['float']['<']   = 'bool'
semantic_cube['float']['float']['>']   = 'bool'
semantic_cube['float']['float']['<=']  = 'bool'
semantic_cube['float']['float']['>=']  = 'bool'
semantic_cube['float']['float']['!=']  = 'bool'
semantic_cube['float']['float']['==']  = 'bool'
semantic_cube['float']['float']['||']  = 'bool'
semantic_cube['float']['float']['&&']  = 'bool'

semantic_cube['char']['char']['=']     = 'bool'
semantic_cube['char']['char']['==']    = 'bool'
semantic_cube['char']['char']['<']     = 'bool'
semantic_cube['char']['char']['>']     = 'bool'
semantic_cube['char']['char']['<=']    = 'bool'
semantic_cube['char']['char']['>=']    = 'bool'
semantic_cube['char']['char']['!=']    = 'bool'
semantic_cube['char']['char']['||']    = 'bool'
semantic_cube['char']['char']['&&']    = 'bool'

semantic_cube['char']['int']['='] = semantic_cube['int']['char']['=']         = 'Error'
semantic_cube['char']['float']['='] = semantic_cube['float']['char']['=']     = 'Error'
semantic_cube['int']['char']['=='] = semantic_cube['char']['int']['==']       = 'Error'
semantic_cube['int']['float']['=='] = semantic_cube['float']['int']['==']       = 'Error'
semantic_cube['float']['char']['=='] = semantic_cube['char']['float']['==']   = 'Error' 
semantic_cube['char']['int']['<'] = semantic_cube['int']['char']['<']         = 'Error'
semantic_cube['char']['float']['<'] = semantic_cube['float']['char']['<']     = 'Error'
semantic_cube['char']['int']['>'] = semantic_cube['int']['char']['>']         = 'Error'
semantic_cube['char']['float']['>'] = semantic_cube['float']['char']['>']     = 'Error'
semantic_cube['char']['int']['<='] = semantic_cube['int']['char']['<=']       = 'Error'
semantic_cube['char']['float']['<='] = semantic_cube['float']['char']['<=']   = 'Error'
semantic_cube['char']['int']['>='] = semantic_cube['int']['char']['>=']       = 'Error'
semantic_cube['char']['float']['>='] = semantic_cube['int']['float']['>=']    = 'Error'
semantic_cube['char']['int']['!='] = semantic_cube['int']['char']['!=']       = 'Error'
semantic_cube['char']['float']['!='] = semantic_cube['float']['char']['!=']   = 'Error'
semantic_cube['char']['int']['||'] = semantic_cube['int']['char']['||']       = 'Error'
semantic_cube['char']['float']['||'] = semantic_cube['char']['float']['||']   = 'Error'
semantic_cube['char']['int']['&&'] = semantic_cube['char']['int']['&&']       = 'Error'
semantic_cube['char']['float']['&&'] = semantic_cube['char']['float']['&&']       = 'Error'