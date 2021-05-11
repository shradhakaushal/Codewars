{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "oppdir = {\"SOUTH\" : \"NORTH\",\n",
    "          \"NORTH\" : \"SOUTH\",\n",
    "          \"WEST\" : \"EAST\",\n",
    "          \"EAST\" : \"WEST\"}\n",
    "\n",
    "def dirReduc(arr):\n",
    "    a = []\n",
    "    for direction in arr:\n",
    "        if a and a[-1] == oppdir[direction]:\n",
    "            a.pop()\n",
    "        else:\n",
    "            a.append(direction)\n",
    "    return (a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
