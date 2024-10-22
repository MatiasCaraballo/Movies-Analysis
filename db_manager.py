{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sqlite3\n",
    "\n",
    "\n",
    "class DatabaseManager:\n",
    "    def __init__(self, db_path):\n",
    "        self.conn = sqlite3.connect(db_path)\n",
    "\n",
    "    def read_data(self, query):\n",
    "        return pd.read_sql_query(query, self.conn)\n",
    "\n",
    "    def close_conn(self):\n",
    "        self.conn.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
