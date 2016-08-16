for i in range(1,10):
    for j in range(1,i+1):
        print(' %d*%d=%d' %(j,i,i*j),end='')
        #end=''的作用是单次打印后不换行
    print()
    #底部迭代完成一次后换行