{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyMFbgAx2HX2uzFacod+GF45",
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
        "<a href=\"https://colab.research.google.com/github/Hwangtaehun/pythonpratice/blob/main/printdatetype.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "go-9pArYB4TW"
      },
      "outputs": [],
      "source": [
        "print(\"hello world!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "자료형"
      ],
      "metadata": {
        "id": "3T6S_09JKYMY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(5)\n",
        "print(-10)\n",
        "print(3.14)\n",
        "print(1000)"
      ],
      "metadata": {
        "id": "C7Q1bNYJDsen"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(5+3)\n",
        "print(2*8)\n",
        "print(6/3)\n",
        "print(3*(3+1))"
      ],
      "metadata": {
        "id": "shovkDODEChw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('풍선')\n",
        "print(\"나비\")\n",
        "print(\"abcdefg\")\n",
        "print(\"10\")\n",
        "print(\"파이썬\"*3)"
      ],
      "metadata": {
        "id": "U-N_ptCREZd0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"I don't want to go to school.\")"
      ],
      "metadata": {
        "id": "dLBSBWwHEveC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "불 자료형"
      ],
      "metadata": {
        "id": "rze0cI2fFIDk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(5>10)\n",
        "print(5<10)"
      ],
      "metadata": {
        "id": "8iySMaSEFDmu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(True)\n",
        "print(False)"
      ],
      "metadata": {
        "id": "YMOf_U1EFOMF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(not True)\n",
        "print(not False)"
      ],
      "metadata": {
        "id": "E6Q9Vgx-FWzN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(not (5>10))"
      ],
      "metadata": {
        "id": "ZH5z_qC-FcKh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "변수"
      ],
      "metadata": {
        "id": "aLN6vksaFsIS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"반려동물을 소개해 주세요.\")\n",
        "print(\"우리 집 반려동물은 개인데, 이름이 연탄이예요.\")\n",
        "print(\"연탄이는 4살이고, 산ㅊ택을 아주 좋아해요.\")\n",
        "print(\"연탄이는 수컷인가요?\")\n",
        "print(\"네.\")"
      ],
      "metadata": {
        "id": "HeDpxf1FFtim"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"연탄이\"\n",
        "animal = \"개\"\n",
        "age = 4\n",
        "hobby = \"산책\"\n",
        "is_male = True\n",
        "\n",
        "print(\"반려동물을 소개해 주세요.\")\n",
        "print(\"우리 집 반려동물은 \" + animal + \"인데, 이름이 \" + name + \"예요.\")\n",
        "print(name + \"는 \" + str(age) + \"살이고, \" + hobby + \"을 아주 좋아해요.\")"
      ],
      "metadata": {
        "id": "tq7RrVhqGJ1-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"해피\"\n",
        "aniaml = \"고양이\"\n",
        "age = 4\n",
        "hobby = \"낮잠\"\n",
        "\n",
        "print(\"반려동물을 소개해 주세요.\")\n",
        "print(\"우리 집 반려동물은 \" + animal + \"인데, 이름이 \" + name + \"예요.\")\n",
        "print(name + \"는 \" + str(age) + \"살이고, \" + hobby + \"을 아주 좋아해요.\")"
      ],
      "metadata": {
        "id": "fXjOMqcFHzNE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"연탄이\"\n",
        "animal = \"개\"\n",
        "age = 4\n",
        "hobby = \"산책\"\n",
        "is_male = True\n",
        "\n",
        "print(\"반려동물을 소개해 주세요.\")\n",
        "print(\"우리 집 반려동물은 \", animal, \"인데, 이름이 \", name, \"예요.\")\n",
        "print(name, \"는 \", age, \"살이고, \", hobby, \"을 아주 좋아해요.\")"
      ],
      "metadata": {
        "id": "6OZ7zx64IIwM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "형변환하기"
      ],
      "metadata": {
        "id": "eLwNVyX4IiS2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(int(\"3\"))\n",
        "#print(int(\"3\") + \"입니다.\")"
      ],
      "metadata": {
        "id": "yYRlbfIbI5yL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(int(3.5))\n",
        "#print(int(\"삼\"))\n",
        "print(float(\"3.5\"))\n",
        "print(float(3))\n",
        "#print(float(\"오\"))\n",
        "print(str(3) + \"입니다.\")\n",
        "print(str(3.5) + \"입니다.\")"
      ],
      "metadata": {
        "id": "UDtkuNccJULV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(3)) #정수\n",
        "print(type(\"3\")) #문자열\n",
        "print(type(3.5)) #실수\n",
        "print(type(str(3))) #정수를 문자열로 형변환"
      ],
      "metadata": {
        "id": "2sO9bbsxJ_KF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}