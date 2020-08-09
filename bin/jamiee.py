
import sys 
import os
import discord
import bin.logic as logic
import bin.database.DBconnector as db
TOKEN=""


def main():
    tmp = db.login() 
    TOKEN = tmp.token




if __name__ == "__main__":
    pass