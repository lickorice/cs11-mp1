Installation
============

The whole game can be copied to your directory
by downloading the source code here_ or by cloning
the git repository like so:

.. code-block:: bash

   git clone http://www.github.com/lickorice/cs11-mp1.git

.. _here: http://www.github.com/lickorice/cs11-mp1

Also, make sure you have **Pygame** installed for *Python 3*.
You can install Pygame through ``pip`` like so:

.. code-block:: bash

   pip3 install pygame

To start the game, run the game through Python 3 in the command terminal
with the following command (given that you are in the root directory of the
program):

.. code-block:: bash

   py -3 main.py

In the absence of Pygame, **the CLI version of the game will boot instead**.

Configuration
=============

Choosing a dictionary
---------------------

In the ``config`` folder of the program, in ``cfg_general.json``, you can change the directory of the
dictionary file to be used. Currently, the game has three built-in dictionaries, ``dictionary_sample.txt``,
``dictionary_small.txt``, and by default, ``dictionary.txt``. Simply change the parameters here:

.. code-block:: json

   {
      "DICTIONARY_FILE": "assets/dictionary.txt"
   }
