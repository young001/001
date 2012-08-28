#incx = 0.0056
#incy = 0.0027
incx = 0.0063
incy = 0.0034
matrix = (10,11)
data_locate = (7,7)
#data = 0.5981
data = 0.7500

x_len = matrix[1]
y_len = matrix[0]

data_x = data_locate[0]
data_y = data_locate[1]

final_data = [[0 for col in range(11)] for row in range(10)]

k = data_y

def output_data(data=data,incx=incx,incy=incy):
    for i in range(data_x):
        final_data[k-1][i] = data+incx*(data_x-i-1)

    for j in range(data_x,x_len):
        final_data[k-1][j] = data -incx*(j-data_x+1)

    for l in range(k,y_len):
        for m in range(x_len):
            final_data[l][m] = final_data[k-1][m]-incy*(l-k+1)


    #print 'final_data[k-1] is',final_data[k-1]
    for n in range(k):
        for m in range(x_len):
            final_data[n][m] = final_data[k-1][m]+incy*(k-n-1)
          
    count = 1
    for i in final_data:
        #print count
        print ['%.4f' %j for j in i]
        print '\n'
        count += 1

if __name__ == '__main__':
    output_data(0.6323,0.0085,0.0048)
    #print '--------------------------------------'
    #output_data()
    #print '--------------------------------------'
    #output_data(0.7777,0.0047,0.0026)



