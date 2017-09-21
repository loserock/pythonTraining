class ClassSample(object):
    """
    This is a sample class,
    counts the number of instances.
    """
    __instances = []
    __instances_number = 0

    def __init__(self, name=None):
        # self.__instances_number += 1
        ClassSample.__instances_number += 1
        self.__name = str(name) if name else str(id(self))
        self.__instances.append(self.__name)

    def __del__(self):
        # self.__instances_number -= 1
        ClassSample.__instances_number -= 1
        self.__instances.remove(self.__name)

    def get_name(self):
        "Return the name of this instance."
        return self.__name

    def get_instance_number(self):
        "Return the number of instances (non static)."
        return self.__instances_number

    def get_instance_list(self):
        "Return the name list of all instances (non static)."
        return self.__instances

    @staticmethod
    def instances_number():
        "Return the number of instances."
        return ClassSample.__instances_number

    @staticmethod
    def instances_name_list():
        "Return the name list of all instances."
        return ClassSample.__instances


class InheritedSample(ClassSample):
    pass


def prety_print(l):
    print "number: {1}\nlist of objects:\n{0}".format(l, len(l))


def main():
    "Main function."
    print dir(ClassSample)
    for d in dir(ClassSample):
        print d, getattr(ClassSample, d)

    print "==============="

    c0 = ClassSample()
    c1 = ClassSample("number two")
    c2 = ClassSample("number three")
    print "constructed:", (c0.get_name(), c1.get_name(), c2.get_name())

    print "==============="

    print c0.get_instance_list()
    print c0.instances_name_list()
    print ClassSample.instances_name_list()
    print "Instance number:\n\
           \t- non static:\t{0}\n\
           \t- static:\t{1}".format(c2.get_instance_number(),
                                    c2.instances_number())

    print "=del %s" % (c2.get_name())
    del c2
    print "Instance number:\n\
        \t- non static:\t{0}\n\
        \t- static:\t{1}".format(c0.get_instance_number(),
                                 c0.instances_number())

    print "=del %s" % (c1.get_name())
    del c1
    print "Instance number:\n\
        \t- non static:\t{0}\n\
        \t- static:\t{1}".format(c0.get_instance_number(),
                                 c0.instances_number())

    print "=del %s" % (c0.get_name())
    del c0

    try:
        print "Instance number:\n\
            \t- non static:\t{0}\n\
            \t- static:\t{1}".format(ClassSample.get_instance_number(),
                                     ClassSample.instances_number())
    except Exception as e:
        print "#", e

    print "Instance number:\n\
        \t- non static:\t{0}\n\
        \t- static:\t{1}".format(ClassSample().get_instance_number(),
                                 ClassSample.instances_number())

    prety_print(ClassSample.instances_name_list())

    c0 = ClassSample("the lonely one")
    l_ref = ClassSample.instances_name_list()
    l_new = list(ClassSample.instances_name_list())

    c0 = ClassSample("the last one")
    prety_print(ClassSample.instances_name_list())
    prety_print(l_ref)
    prety_print(l_new)


if __name__ == "__main__":
    main()
    print "\n== main() ended ==\n"
    try:
        prety_print(l_new)
    except Exception as e:
        print "#", e
    prety_print(ClassSample.instances_name_list())

    c1 = ClassSample('original')
    i1 = InheritedSample('inherited')
    prety_print(ClassSample.instances_name_list())
    prety_print(InheritedSample.instances_name_list())
    prety_print(i1.get_instance_list())
