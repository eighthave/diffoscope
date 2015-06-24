#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# debbindiff: highlight differences between two builds of Debian packages
#
# Copyright © 2015 Jérémy Bobbio <lunar@debian.org>
#
# debbindiff is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# debbindiff is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with debbindiff.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import shutil
import pytest
from debbindiff.comparators.pdf import compare_pdf_files

TEST_FILE1_PATH = os.path.join(os.path.dirname(__file__), '../data/test1.pdf') 
TEST_FILE2_PATH = os.path.join(os.path.dirname(__file__), '../data/test2.pdf') 

def test_no_differences():
    differences = compare_pdf_files(TEST_FILE1_PATH, TEST_FILE1_PATH)
    assert len(differences) == 0

@pytest.fixture
def differences():
    return compare_pdf_files(TEST_FILE1_PATH, TEST_FILE2_PATH)[0].details # skip container with path

def test_text_diff(differences):
    expected_diff = open(os.path.join(os.path.dirname(__file__), '../data/pdf_text_expected_diff')).read()
    assert differences[0].unified_diff == expected_diff

def test_internal_diff(differences):
    expected_diff = open(os.path.join(os.path.dirname(__file__), '../data/pdf_internal_expected_diff')).read()
    assert differences[1].unified_diff == expected_diff