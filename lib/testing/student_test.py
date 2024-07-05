# lib/testing/student_test.py
import pytest
from lib.student import Student
from lib.chatty_student import ChattyStudent

def test_student_hello(capfd):
    student = Student()
    student.hello()
    captured = capfd.readouterr()
    assert captured.out == "Hey there! I'm so excited to learn stuff.\n"

def test_student_raise_hand(capfd):
    student = Student()
    student.raise_hand()
    captured = capfd.readouterr()
    assert captured.out == "Pick me!\n"

def test_chatty_student_hello(capfd):
    chatty_student = ChattyStudent()
    chatty_student.hello()
    captured = capfd.readouterr()
    expected_output = ("Hey there! I'm so excited to learn stuff.\n"
                       "How are you doing today? I'm okay, but I'm kind of tired. "
                       "Did you watch The Walking Dead last night? You didn't?! "
                       "Oh man, it was so crazy! What, you don't want any spoilers? "
                       "Okay well let me just tell you who died...\n")
    assert captured.out == expected_output

def test_chatty_student_raise_hand(capfd):
    chatty_student = ChattyStudent()
    chatty_student.raise_hand()
    captured = capfd.readouterr()
    assert captured.out == ("Pick me!\n" * 10)
