from test_text_plot import is_array
from test_text_plot import each_element_number

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
    """

    assert is_array(x), 'First argument is not a list/tuple'
    assert is_array(y), 'Second argument is not a list/tuple'
    assert len(x)==len(y), 'Length of first and second arguments must be same'
    assert each_element_number(x), 'Every element in the first argument is not number'
    assert each_element_number(y), 'Every element in the second argument is not number'
    
    each_div_x=float(max(x)-min(x))/screen_size[0]
    each_div_y=float(max(y)-min(y))/screen_size[1]
    print_list=[]
    for i in range(screen_size[0]):
        new=[]
        for j in range(screen_size[1]):
            new.append(' ')
        print_list.append(new)
    for i in range(len(x)):
        x_to_plot=int((x[i]-min(x))/each_div_x)
        if(x_to_plot>screen_size[0]-1):
            x_to_plot=screen_size[0]-1
        y_to_plot=int((y[i]-min(y))/each_div_y)
        if(y_to_plot>screen_size[1]-1):
            y_to_plot=screen_size[1]-1
        #print x_to_plot," ",y_to_plot
        print_list[x_to_plot][y_to_plot]='*'
    for j in reversed(range(screen_size[1])):
        print "%2d|" %j,
        for i in range(screen_size[0]):
            print print_list[i][j],
        print ""
    #print "   ",
    #for j in range(screen_size[0]):
    #    print "_",
    #print ""
    #print "   ",
    #for j in range(screen_size[0]):
    #    print j/10,
    #print ""
    #print "   ",
    #for j in range(screen_size[0]):
    #    print j%10,
    #    

if __name__=='__main__':
    import math
    print "Default screen size is (30,20). Want to tweak it? [y/n]"
    user_input=raw_input()
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
    plot(x_list_copy,y_list_copy,default_screen_size)



def each_element_number(lst):
    var_to_return=True
    for each in lst:
        var=isinstance(each, (int, float, long))
        if var==False:
            var_to_return=False
    return(var_to_return)
