#from test_text_plot import is_array
#from test_text_plot import each_element_number

def each_element_number(lst):
    """Checks if each element of the list/tuple is number or not
    each_element_number(lst)
    """
    var_to_return=True
    for each in lst:
        var=isinstance(each, (int, float, long))
        if var==False:
            var_to_return=False
    return(var_to_return)


def is_array(var):
    """Checks if the array given is list/tuple type. If any other type is given as input, then raises an error
    """
    try:
        isArray=list(var)
    except ValueError:
        print "ValueError"
    except TypeError:
        print "The variable is not a list"
    finally:
        pass
    return isinstance(var, (list, tuple))

def is_len_equal(a,b):
    """Checks if the length of two lists given is same or not"""
    return len(a)==len(b)

def get_canvas(screen_size):
    """Creating a blank canvas that can be printed. 
    Resolution of the canvas is given by optional input argument screen_size
    """
    print_list=[]
    for i in range(screen_size[0]):
        new=[]
        for j in range(screen_size[1]):
            new.append(' ')
        print_list.append(new)
    return print_list

def modify_canvas(x,y,print_list,screen_size):
    """Depending on the input lists/tuples, canvas is modified with '*'"""
    each_div_x=float(max(x)-min(x))/screen_size[0]
    each_div_y=float(max(y)-min(y))/screen_size[1]
    for i in range(len(x)):
        x_to_plot=int((x[i]-min(x))/each_div_x)
        if(x_to_plot>screen_size[0]-1):
            x_to_plot=screen_size[0]-1
        y_to_plot=int((y[i]-min(y))/each_div_y)
        if(y_to_plot>screen_size[1]-1):
            y_to_plot=screen_size[1]-1
        #print x_to_plot," ",y_to_plot
        print_list[x_to_plot][y_to_plot]='*'
    return print_list

def assertions(x,y,screen_size):
    """Checking all assertions"""
    assert is_array(x), 'First argument is not a list/tuple'
    assert is_array(y), 'Second argument is not a list/tuple'
    assert is_len_equal(x,y), 'Length of first and second arguments must be same'
    assert each_element_number(x), 'Every element in the first argument is not number'
    assert each_element_number(y), 'Every element in the second argument is not number'
    assert is_array(screen_size), 'Screen size is not an array'
    assert len(screen_size)==2, 'Screen size must have only two elements'
    assert each_element_number(screen_size), 'Screen size must consist only numbers'
    if len(x)>screen_size[0]:
        print 'Data is more than the screen size. Data may be lost'


def plot(x,y,screen_size=(40,40)):
    """Plots the x-y pairs in the given screen resolution

    Arguments:
    x: list/tuple containing x coordinates
    y: list/tuple containing y coordinates
    Both x and y list must contain same number of elements. Also, 
    both the lists must contain only integers/floats

    Third argument: [optional]
    Tuple which contains (width, height)
    Default is (40,40)

    Example: 
    x=(3,14,21.4,1,-4,2.5)
    y=(1,0,3,5.3,1.5,10)
    screen_res=(40,40)
    plot(x,y,screen_res)
    
    Make sure x and y are tuples/lists. Arrays, if generated using scipy must be converted to list/tuple.
    """
    print "If screen_size is not given as an argument, then default (40x40) will be taken"
    assertions(x,y,screen_size)
    print_list=get_canvas(screen_size)
    print_list=modify_canvas(x,y,print_list,screen_size)
    for j in reversed(range(screen_size[1])):
        print "%2d|" %j,
        for i in range(screen_size[0]):
            print print_list[i][j],
        print ""

if __name__=='__main__':
    #If __main__, then run the following
    import math
    print "Default screen size is (30,20). Want to tweak it? [y/n]"
    user_input=raw_input() #Changing the screen_size (plot canvas)
    if user_input=='y':
        while True:
            try:
                default_screen_size_x=int(raw_input('Give x coordinate:'))
                break
            except ValueError:
                print "Invalid Number! Try again..."
        while True:
            try:
                default_screen_size_y=int(raw_input('Give y coordinate:'))
                break
            except ValueError:
                print "Invalid Number! Try again..."
        default_screen_size=(default_screen_size_x, default_screen_size_y)
    else:
        default_screen_size=(30,20) 
    #Calculating the 'x' and 'y' list for sine wave plot. 
    #Note that there is no functions from scipy used here.
    x_max=2*math.pi
    y_max=2*math.sin(math.pi/2)
    x_resolution=x_max/default_screen_size[0]
    y_resolution=y_max/default_screen_size[1]
    x_list=[]
    y_list=[]
    for i in range(default_screen_size[0]):
        x_list.append(x_resolution*i)
        y_list.append(math.sin(x_resolution*i))
    x_list_copy=x_list
    y_list_copy=y_list
    #The following line plots the sine wave
    plot(x_list_copy,y_list_copy,default_screen_size)
