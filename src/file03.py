# -*-coding:utf-8-*-

class Test1():
    '''
    我是测试类，负责测试
    '''

    def hello3(self):
        '''
        负责打印Hello， 人人可以学Python

        这个函数是自编函数，主要用来计算两个函数的和

        :return:

        Examples:
            >>> c = my_add(1,2)
            >>> print('Xdd')
                Xdd
        '''
        print("人人可以学Python")

    def renren3(self):
        '''
        测试Sphinx自动生成文档 ``test_23``

        :return:

        Examples:
            >>>
            c = my_add(1,2)
            print('Xdd')
        '''
        print("自动生成文档")


class Test23():

    def test_23(self):
        '''
        我也不知道写什么好，反正我们这里是用来写文档的

        :return:
        '''
        print("文档自动生成测试2")

    def renren_23(self):
        '''
        所以我们开发的时候就应该在这里写好文档，然后用Sphinx自动生成

        :return:
        '''
        print("自动生成文档2")
