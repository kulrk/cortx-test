#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2022 Seagate Technology LLC and/or its Affiliates
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.
#

"""IO TestSet Process Schedular Unit Testing"""
import time
from multiprocessing import cpu_count

from src.libs.io_schedular import main


test_results = {}


# TestGroup


class TestSet1:
    """ TestSet1 """

    @staticmethod
    def test1():
        """testcase"""
        time.sleep(2)
        test_results["TestSet1->Test1"] = "Executed"
        return "TestSet1->Test1"

    @staticmethod
    def test2():
        """testcase"""
        time.sleep(2)
        test_results["TestSet1->Test2"] = "Executed"
        return "TestSet1->Test2"


class TestSet2:
    """ TestSet2 """

    @staticmethod
    def test1():
        """testcase"""
        time.sleep(2)
        test_results["TestSet2->Test1"] = "Executed"
        return "TestSet2->Test1"

    @staticmethod
    def test2():
        """testcase"""
        time.sleep(2)
        test_results["TestSet2->Test2"] = "Executed"
        return "TestSet2->Test2"


class TestSet3:
    """ testSet3 """

    @staticmethod
    def test1():
        """testcase"""
        time.sleep(2)
        test_results["TestSet3->Test1"] = "Executed"
        return "TestSet3->Test1"

    @staticmethod
    def test2():
        """testcase"""
        time.sleep(2)
        test_results["TestSet3->Test2"] = "Executed"
        return "TestSet3->Test2"


class TestSet4:
    """ TestSet4 """

    @staticmethod
    def test1():
        """testcase"""
        time.sleep(2)
        test_results["TestSet4->Test1"] = "Executed"
        return "TestSet4->Test1"

    @staticmethod
    def test2():
        """testcase"""
        time.sleep(2)
        test_results["TestSet4->Test2"] = "Executed"
        return "TestSet4->Test2"


class TestSet5:
    """ TestSet5 """

    @staticmethod
    def test1():
        """testcase"""
        time.sleep(2)
        test_results["TestSet5->Test1"] = "Executed"
        return "TestSet5->Test1"

    @staticmethod
    def test2():
        """testcase"""
        time.sleep(2)
        test_results["TestSet5->Test2"] = "Executed"
        return "TestSet5->Test2"


class TestSet6:
    """ TestSet6 """

    @staticmethod
    def test1():
        """testcase"""
        time.sleep(2)
        test_results["TestSet6->Test1"] = "Executed"
        return "TestSet6->Test1"

    @staticmethod
    def test2():
        """testcase"""
        time.sleep(2)
        test_results["TestSet6->Test2"] = "Executed"
        return "TestSet6->Test2"


if __name__ == '__main__':
    SuiteList = ['TestSet1', 'TestSet2', 'TestSet3', 'TestSet4', 'TestSet5', 'TestSet6']
    print("Executing Following Suites", SuiteList)
    print("\n")
    try:
        WORKERS = cpu_count()
    except NotImplementedError:
        WORKERS = 1
    print("Number of workers", WORKERS)
    t = time.time()
    main(SuiteList, WORKERS)
    print("Total Execution Time Taken", time.time() - t)