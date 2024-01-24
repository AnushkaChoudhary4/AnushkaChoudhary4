{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNexqv2mbNv5GKDh5uv5wiO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AnushkaChoudhary4/AnushkaChoudhary4/blob/main/list%20and%20tuple.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N_rQOl3siYws",
        "outputId": "adb5939a-b6fc-4a93-e5b4-2f7fbe45e10b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter numbers seprated by space:3 4 78 56\n",
            "the largest number is: 78\n"
          ]
        }
      ],
      "source": [
        "user_input=input(\"enter numbers seprated by space:\")\n",
        "user_list=[int(element) for element in user_input.split()]\n",
        "largest_number=max(user_list)\n",
        "print(\"the largest number is:\",largest_number)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tuple=('pihu','anu','kanu')\n",
        "print(tuple)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s-z2oZ98mDTO",
        "outputId": "a5cf010b-5ffc-4c2a-edf9-f23bf3eb5eae"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('pihu', 'anu', 'kanu')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tuple_result=('priyanka')\n",
        "print(tuple_result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "51qrAuk1mqx3",
        "outputId": "de931350-4e6f-4834-e57e-ea65ac6e95e5"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "priyanka\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s=(4,5,6)\n",
        "s_append=s +(2,3,4)\n",
        "print(s_append)\n",
        "print(s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fVfOH_Rgoy-D",
        "outputId": "aae82ac5-7036-4b63-d916-7921c1d483ea"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(4, 5, 6, 2, 3, 4)\n",
            "(4, 5, 6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tup=('priyanka','pihu')\n",
        "del tup\n",
        "print(\"after deleting\")\n",
        "print('anu')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KXHqIMArp20z",
        "outputId": "3d630066-e64d-4e94-b9bd-c43d3fffe1f4"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "after deleting\n",
            "anu\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tuple=('anu','pihu','kanu')\n",
        "tuple.index('pihu')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fveBxmEFqaH3",
        "outputId": "5f6b7358-1ae8-4e8e-c8a8-d226e884fef6"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fruits=('mango','grapes','banana','banana')\n",
        "res=[]\n",
        "for j in range(len(fruits)):\n",
        "  my_fruit=fruits[j]\n",
        "  count=0\n",
        "  for i in range(len(fruits)):\n",
        "      if i==j:\n",
        "        continue\n",
        "      if fruits[i]==fruits[j]:\n",
        "        count+=1\n",
        "  if count>0:\n",
        "    if my_fruit not in res:\n",
        "      res.append(my_fruit)\n",
        "print(res)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CXR9taOsrrBo",
        "outputId": "4a0c0766-be20-4840-d5fb-397e8155ffaa"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['banana']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lst = ['Iris', 'Orchids', 'Rose', 'Lavender',\n",
        "    'Lily', 'Carnations']\n",
        "print(\"Original List is :\", lst)\n",
        "\n",
        "lst.remove('Orchids')\n",
        "print(\"After deleting the item :\", lst)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G5lpWVthwDcW",
        "outputId": "11de28a8-1ea5-4e2b-f73e-e6d58f3d4d47"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original List is : ['Iris', 'Orchids', 'Rose', 'Lavender', 'Lily', 'Carnations']\n",
            "After deleting the item : ['Iris', 'Rose', 'Lavender', 'Lily', 'Carnations']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mylist = [10, 20, 30, 40, 50]\n",
        "print(\"Original list: \",mylist)\n",
        "mylist[2] = 35\n",
        "print(\"After updating list is:\", mylist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WmCTR1tcwv5_",
        "outputId": "c4b076e1-e14d-4421-e474-777de5d4a0ed"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original list:  [10, 20, 30, 40, 50]\n",
            "After updating list is: [10, 20, 35, 40, 50]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fruits = ['apple', 'banana', 'cherry']\n",
        "\n",
        "fruits.insert(1, \"orange\")\n"
      ],
      "metadata": {
        "id": "vJwM_fJkx1bt"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tuples=(0,2,4,6,8)\n",
        "print(\"original tuple:\",tuples)\n",
        "mylist=list(tuple)\n",
        "print(\"convert type to list\",mylist)\n",
        "print(\"type\",type(mylist))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d7fZ1BhiyF1S",
        "outputId": "8a75c868-6f71-422f-da39-eaaf5f1e84c5"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "original tuple: (0, 2, 4, 6, 8)\n",
            "convert type to list ['anu', 'pihu', 'kanu']\n",
            "type <class 'list'>\n"
          ]
        }
      ]
    }
  ]
}