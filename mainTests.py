import unittest
import random

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

        self.assertIsNotNone(info["tasks"])
        self.assertIsNotNone(info["people"])

        firstPerson = info["people"][0]
        firstTask = info["tasks"][0]

        # Could combine these into "person fields failed..." or something more generic
        try:
            a = firstPerson["uniqueID"]
        except NameError:
            print("person uniqueID field failed")
            self.assertTrue(False)

        try:
            a = firstPerson["capacity"]
        except NameError:
            print("person capacity field failed")
            self.assertTrue(False)
        try:
            a = firstPerson["taskAvail"]
        except NameError:
            print("person taskAvail field failed")
            self.assertTrue(False)

        try:
            a = firstPerson["tags"]
        except NameError:
            print("person tags field failed")
            self.assertTrue(False)

        try:
            a = firstTask["uniqueID"]
        except NameError:
            print("task uniqueID field failed")
            self.assertTrue(False)

        try:
            a = firstTask["estimate"]
        except NameError:
            print("task estimate field failed")
            self.assertTrue(False)

        try:
            a = firstTask["devAvail"]
        except NameError:
            print("task devAvail field failed")
            self.assertTrue(False)

        try:
            a = firstTask["tags"]
        except NameError:
            print("tags field failed")
            self.assertTrue(False)

        try:
            a = firstTask["child"]
        except NameError:
            print("task child field failed")
            self.assertTrue(False)

        try:
            a = firstTask["parent"]
        except NameError:
            print("task parent field failed")
            self.assertTrue(False)

        try:
            a = firstTask["dependsOn"]
        except NameError:
            print("task dependsOn field failed")
            self.assertTrue(False)

        try:
            a = firstTask["dependedBy"]
        except NameError:
            print("task dependedBy field failed")
            self.assertTrue(False)

    def testTaskLinkTraversal(self):
        # - Check if dependency/child tasks can be traversed up/down
        tasks = self.algoInput.tasks
        # value is dictionary of x [key] y. IE: Task 1 dependsOn Task 2
        expectedOutput = {"dependsOn":1,"dependedBy":2,"child":3,"parent":4}
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
        expectedCapacity = 111111
        expectedTaskEstimate = 11111
        exepctedDifference = expectedCapacity - expectedTaskEstimate

        peopleArr = self.algoInput.people
        # sum up all peopleArr.capacity
        capacity = 0
        for person in self.algoInput.people:
            capacity += person["capacity"]

        # sum up all tasks.capacity
        taskEstimate = 0
        for task in self.algoInput.tasks:
            taskEstimate += task["estimate"]

        self.assertEqual(expectedCapacity, capacity)
        self.assertEqual(expectedTaskEstimate, taskEstimate)

    def testDevTaskMatching(self):
        # - Does developer task matching work?
        self.algorithm.matchNecessaries() # object includes available people/matches and such

        self.assertTrue(self.algorithm.people["Bob"].assignedTask != None)
        self.assertTrue(self.algorithm.people["Jill"].assignedTask != None)

        self.algorithm.resetMatches() # reset what we have matched

    def testEasySolution(self):
        # - Can we complete a solution (given easy problem?)

        random.seed(17)
        self.algorithm.randomSearch() # find random solution

        # check if it meets known constraints. This will be basis for constraint checking a generic solution.
        self.assertTrue(self.algorithm.checkHardConstraints())

    def tearDown(self):
        try:
            self.algoInput = None
            self.algorithm = None
            self.people = None
            self.tasks = None
            print("teardown succeed")
        except NameError:
            print("Teardown failed")

if __name__ == '__main__':
    unittest.main()
