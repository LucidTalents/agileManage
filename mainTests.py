import unittest


class TestInput(unittest.TestCase):
    def setUp(self):
        # Assume meeting output, and then test characteristics using algos, but I know expected output (by manual assert)
        try:
            #self.jsonFile = json.import()
            self.algoInput = AlgoInput(self.jsonFile)  # algo input class. Has people, tasks, childs, dependencies, etc.
            self.algorithm = Algorithm(self.algoInput)  # algorithm class. available people, capacity, unmatched people,capcity, etc.
            print("setup succeed")
        except NameError:
            print("Setup failed")

    def testAlgoInput(self):
        # - Intake of meeting input (expected: all necessary variables are there)
        info = self.algoInput.info  # from JSON File
        # Get all keys from json
        # check if all keys present -> indicates form considered correct information.
        #!= None
        info["tasks"]
        info["people"]

        firstPerson = info["people"][0]
        firstTask = info["tasks"][0]
        firstPerson["uniqueID"]
        firstPerson["capacity"]
        firstPerson["taskAvail"]
        firstPerson["tags"]

        firstTask["uniqueID"]
        firstTask["estimate"]
        firstTask["devAvail"]
        firstTask["tags"]

        firstTask["child"]
        firstTask["parent"]
        firstTask["dependsOn"]
        firstTask["dependedBy"]

        self.assertEqual(True, True)

    def testTaskLinkTraversal(self):
        # - Check if dependency/child tasks can be traversed up/down
        tasks = self.algoInput.tasks
        # value is dictionary of x [key] y. IE: Task 1 dependsOn Task 2
        expectedOutput = {"dependsOn":1,"dependedBy":2,"child":3,"parent",4}
        for key,value in expectedOutput:
            expectedOutput[key] = sorted(expectedOutput[key])

        output = {key: None for key in ["dependsOn","dependedBy","child","parent"]}

        #Add to each category.
        for task in tasks:
            id = task["uniqueID"]
            if (task["dependsOn"] != None): output["dependsOn"][id] = task["dependsOn"]
            if (task["dependedBy"] != None): output["dependedBy"][id] = task["dependedBy"]
            if (task["child"] != None): output["child"][id] = task["child"]
            if (task["parent"] != None): output["parent"][id] = task["parent"]

        # Sort
        for key,value in output:
            output[key] = sorted(output[key])

        self.assertEqual(expectedOutput, output)

    def testCapacity(self):
        # - Check algorithm points mapping and capacity (does mapping occur correctly? Do we aggregate
        # capacity and determine leftover capacity correctly?)
        peopleArr = self.algoInput.people
        # sum up all peopleArr.capacity
        # sum up all tasks.capacity
        # determine leftover
        # should do manually and check against that
        self.assertEqual(True, True)

    def testDevTaskMatching(self):
        # - Does developer task matching work?
        self.algorithm.matchNecessaries() # object includes available people/matches and such

        # return list of matches
        # compare with expected list.
        self.assertEqual(True, True)

    def testEasySolution(self):
        # - Can we complete a solution (given easy problem?)

        # do random algorithm (perm seed so it is the same every time for the test)
        # check if it meets known constraints. This will be basis for constraint checking a generic solution.
        self.assertEqual(True, True)

    def tearDown(self):
        try:
            self.algoInput = None
            self.algorithm = None
            self.people = None
            self.tasks = None
            print("teardown succeed")
        except NameError:
            print("Teardown failed")


'''
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''
if __name__ == '__main__':
    unittest.main()
