#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()
        
        
    def test_help(self):
        """Testing help option"""
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout = subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout.decode("utf8"), usage)
        
        
    def test_upper_short(self):
        """Testing upper short option"""
        args = ["-u", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")
        
        
    def test_upper_long(self):
        """Testing upper long option"""
        args = ["--upper", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")
        
        
    def test_lower_short(self):
        """Testing lower short option"""
        args = ["-l", "heLLo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, "hello")
        
        
    def test_lower_long(self):
        """Testing lower long option"""
        args = ["--lower", "heLLo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, "hello")
        
        
    def test_title_short(self):
        """Testing title short option"""
        args = ["-t", "hi folks!"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEquals(result, "Hi Folks!")
        
        
    def test_title_long(self):
        """Testing title short option"""
        args = ["--title", "hi folks!"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEquals(result, "Hi Folks!")
        
        
    def test_all(self):
        """Testing all args"""
        args = ["-tul", "heLLo!"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO!")
        
        
    def test_two_args(self):
        """Testing TWO args"""
        args = ["-tl", "heLLo!"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, "hello!")
        
        
    def test_no_args(self):
        """Testing NO args"""
        args = ["Hello!"]
        result = echo.main(args)
        self.assertEquals(result, 'Hello!')
        
        
if __name__ == '__main__':
    unittest.main()
    