# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 2.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExceptionsPlatformErrorCodes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"
    _10 = "10"
    _11 = "11"
    _12 = "12"
    _13 = "13"
    _14 = "14"
    _15 = "15"
    _16 = "16"
    _17 = "17"
    _18 = "18"
    _19 = "19"
    _20 = "20"
    _21 = "21"
    _22 = "22"
    _23 = "23"
    _24 = "24"
    _25 = "25"
    _26 = "26"
    _27 = "27"
    _28 = "28"
    _29 = "29"
    _30 = "30"
    _31 = "31"
    _32 = "32"
    _33 = "33"
    _34 = "34"
    _35 = "35"
    _36 = "36"
    _37 = "37"
    _38 = "38"
    _39 = "39"
    _40 = "40"
    _41 = "41"
    _42 = "42"
    _43 = "43"
    _44 = "44"
    _45 = "45"
    _46 = "46"
    _47 = "47"
    _48 = "48"
    _49 = "49"
    _50 = "50"
    _51 = "51"
    _52 = "52"
    _89 = "89"
    _90 = "90"
    _91 = "91"
    _92 = "92"
    _93 = "93"
    _94 = "94"
    _95 = "95"
    _96 = "96"
    _97 = "97"
    _98 = "98"
    _99 = "99"
    _100 = "100"
    _101 = "101"
    _102 = "102"
    _103 = "103"
    _104 = "104"
    _105 = "105"
    _106 = "106"
    _107 = "107"
    _108 = "108"
    _109 = "109"
    _110 = "110"
    _111 = "111"
    _112 = "112"
    _113 = "113"
    _115 = "115"
    _116 = "116"
    _117 = "117"
    _118 = "118"
    _119 = "119"
    _120 = "120"
    _121 = "121"
    _122 = "122"
    _123 = "123"
    _124 = "124"
    _125 = "125"
    _126 = "126"
    _127 = "127"
    _128 = "128"
    _129 = "129"
    _130 = "130"
    _131 = "131"
    _132 = "132"
    _133 = "133"
    _134 = "134"
    _135 = "135"
    _136 = "136"
    _137 = "137"
    _138 = "138"
    _139 = "139"
    _140 = "140"
    _141 = "141"
    _142 = "142"
    _143 = "143"
    _144 = "144"
    _145 = "145"
    _146 = "146"
    _147 = "147"
    _148 = "148"
    _149 = "149"
    _150 = "150"
    _151 = "151"
    _152 = "152"
    _153 = "153"
    _154 = "154"
    _155 = "155"
    _156 = "156"
    _157 = "157"
    _158 = "158"
    _159 = "159"
    _160 = "160"
    _161 = "161"
    _162 = "162"
    _163 = "163"
    _164 = "164"
    _165 = "165"
    _166 = "166"
    _167 = "167"
    _168 = "168"
    _169 = "169"
    _170 = "170"
    _171 = "171"
    _172 = "172"
    _173 = "173"
    _174 = "174"
    _175 = "175"
    _200 = "200"
    _201 = "201"
    _202 = "202"
    _203 = "203"
    _204 = "204"
    _205 = "205"
    _206 = "206"
    _207 = "207"
    _208 = "208"
    _209 = "209"
    _210 = "210"
    _211 = "211"
    _212 = "212"
    _213 = "213"
    _214 = "214"
    _215 = "215"
    _216 = "216"
    _217 = "217"
    _218 = "218"
    _219 = "219"
    _220 = "220"
    _221 = "221"
    _222 = "222"
    _223 = "223"
    _224 = "224"
    _225 = "225"
    _226 = "226"
    _227 = "227"
    _300 = "300"
    _301 = "301"
    _302 = "302"
    _303 = "303"
    _304 = "304"
    _305 = "305"
    _306 = "306"
    _307 = "307"
    _308 = "308"
    _309 = "309"
    _310 = "310"
    _311 = "311"
    _312 = "312"
    _400 = "400"
    _500 = "500"
    _501 = "501"
    _502 = "502"
    _503 = "503"
    _504 = "504"
    _505 = "505"
    _506 = "506"
    _507 = "507"
    _508 = "508"
    _509 = "509"
    _510 = "510"
    _511 = "511"
    _512 = "512"
    _513 = "513"
    _514 = "514"
    _515 = "515"
    _516 = "516"
    _517 = "517"
    _518 = "518"
    _519 = "519"
    _520 = "520"
    _521 = "521"
    _522 = "522"
    _523 = "523"
    _524 = "524"
    _525 = "525"
    _526 = "526"
    _527 = "527"
    _528 = "528"
    _529 = "529"
    _530 = "530"
    _531 = "531"
    _532 = "532"
    _533 = "533"
    _534 = "534"
    _535 = "535"
    _536 = "536"
    _537 = "537"
    _538 = "538"
    _539 = "539"
    _540 = "540"
    _541 = "541"
    _542 = "542"
    _543 = "543"
    _544 = "544"
    _555 = "555"
    _556 = "556"
    _557 = "557"
    _558 = "558"
    _559 = "559"
    _560 = "560"
    _561 = "561"
    _562 = "562"
    _563 = "563"
    _564 = "564"
    _565 = "565"
    _566 = "566"
    _567 = "567"
    _568 = "568"
    _569 = "569"
    _570 = "570"
    _571 = "571"
    _572 = "572"
    _573 = "573"
    _574 = "574"
    _575 = "575"
    _576 = "576"
    _577 = "577"
    _578 = "578"
    _579 = "579"
    _580 = "580"
    _581 = "581"
    _582 = "582"
    _583 = "583"
    _584 = "584"
    _585 = "585"
    _586 = "586"
    _587 = "587"
    _588 = "588"
    _589 = "589"
    _590 = "590"
    _591 = "591"
    _592 = "592"
    _593 = "593"
    _594 = "594"
    _601 = "601"
    _602 = "602"
    _603 = "603"
    _604 = "604"
    _605 = "605"
    _606 = "606"
    _607 = "607"
    _608 = "608"
    _609 = "609"
    _610 = "610"
    _611 = "611"
    _612 = "612"
    _613 = "613"
    _614 = "614"
    _615 = "615"
    _616 = "616"
    _617 = "617"
    _618 = "618"
    _619 = "619"
    _620 = "620"
    _621 = "621"
    _622 = "622"
    _623 = "623"
    _624 = "624"
    _625 = "625"
    _626 = "626"
    _627 = "627"
    _628 = "628"
    _629 = "629"
    _630 = "630"
    _631 = "631"
    _632 = "632"
    _633 = "633"
    _634 = "634"
    _635 = "635"
    _636 = "636"
    _637 = "637"
    _638 = "638"
    _639 = "639"
    _641 = "641"
    _642 = "642"
    _643 = "643"
    _644 = "644"
    _646 = "646"
    _647 = "647"
    _648 = "648"
    _649 = "649"
    _650 = "650"
    _651 = "651"
    _652 = "652"
    _653 = "653"
    _654 = "654"
    _655 = "655"
    _656 = "656"
    _657 = "657"
    _658 = "658"
    _659 = "659"
    _660 = "660"
    _661 = "661"
    _662 = "662"
    _663 = "663"
    _664 = "664"
    _665 = "665"
    _666 = "666"
    _667 = "667"
    _668 = "668"
    _669 = "669"
    _670 = "670"
    _671 = "671"
    _672 = "672"
    _673 = "673"
    _674 = "674"
    _675 = "675"
    _676 = "676"
    _677 = "677"
    _678 = "678"
    _679 = "679"
    _680 = "680"
    _681 = "681"
    _682 = "682"
    _683 = "683"
    _684 = "684"
    _685 = "685"
    _686 = "686"
    _687 = "687"
    _688 = "688"
    _689 = "689"
    _690 = "690"
    _691 = "691"
    _692 = "692"
    _693 = "693"
    _694 = "694"
    _695 = "695"
    _696 = "696"
    _697 = "697"
    _698 = "698"
    _699 = "699"
    _701 = "701"
    _702 = "702"
    _703 = "703"
    _704 = "704"
    _705 = "705"
    _706 = "706"
    _707 = "707"
    _801 = "801"
    _802 = "802"
    _803 = "803"
    _804 = "804"
    _805 = "805"
    _806 = "806"
    _807 = "807"
    _900 = "900"
    _901 = "901"
    _902 = "902"
    _903 = "903"
    _904 = "904"
    _905 = "905"
    _906 = "906"
    _907 = "907"
    _908 = "908"
    _909 = "909"
    _1000 = "1000"
    _1001 = "1001"
    _1002 = "1002"
    _1003 = "1003"
    _1004 = "1004"
    _1005 = "1005"
    _1006 = "1006"
    _1007 = "1007"
    _1008 = "1008"
    _1009 = "1009"
    _1100 = "1100"
    _1204 = "1204"
    _1205 = "1205"
    _1218 = "1218"
    _1223 = "1223"
    _1224 = "1224"
    _1225 = "1225"
    _1226 = "1226"
    _1227 = "1227"
    _1229 = "1229"
    _1230 = "1230"
    _1231 = "1231"
    _1232 = "1232"
    _1233 = "1233"
    _1234 = "1234"
    _1235 = "1235"
    _1236 = "1236"
    _1237 = "1237"
    _1300 = "1300"
    _1301 = "1301"
    _1302 = "1302"
    _1303 = "1303"
    _1304 = "1304"
    _1305 = "1305"
    _1306 = "1306"
    _1307 = "1307"
    _1308 = "1308"
    _1309 = "1309"
    _1310 = "1310"
    _1311 = "1311"
    _1312 = "1312"
    _1313 = "1313"
    _1314 = "1314"
    _1315 = "1315"
    _1316 = "1316"
    _1317 = "1317"
    _1318 = "1318"
    _1400 = "1400"
    _1401 = "1401"
    _1402 = "1402"
    _1403 = "1403"
    _1404 = "1404"
    _1405 = "1405"
    _1500 = "1500"
    _1501 = "1501"
    _1502 = "1502"
    _1600 = "1600"
    _1601 = "1601"
    _1602 = "1602"
    _1603 = "1603"
    _1604 = "1604"
    _1605 = "1605"
    _1606 = "1606"
    _1607 = "1607"
    _1608 = "1608"
    _1609 = "1609"
    _1610 = "1610"
    _1611 = "1611"
    _1612 = "1612"
    _1613 = "1613"
    _1614 = "1614"
    _1615 = "1615"
    _1616 = "1616"
    _1617 = "1617"
    _1618 = "1618"
    _1619 = "1619"
    _1620 = "1620"
    _1621 = "1621"
    _1622 = "1622"
    _1623 = "1623"
    _1624 = "1624"
    _1625 = "1625"
    _1626 = "1626"
    _1627 = "1627"
    _1628 = "1628"
    _1629 = "1629"
    _1630 = "1630"
    _1631 = "1631"
    _1632 = "1632"
    _1633 = "1633"
    _1634 = "1634"
    _1635 = "1635"
    _1636 = "1636"
    _1637 = "1637"
    _1638 = "1638"
    _1639 = "1639"
    _1640 = "1640"
    _1641 = "1641"
    _1642 = "1642"
    _1643 = "1643"
    _1644 = "1644"
    _1645 = "1645"
    _1646 = "1646"
    _1647 = "1647"
    _1648 = "1648"
    _1649 = "1649"
    _1650 = "1650"
    _1651 = "1651"
    _1652 = "1652"
    _1653 = "1653"
    _1654 = "1654"
    _1655 = "1655"
    _1656 = "1656"
    _1657 = "1657"
    _1658 = "1658"
    _1659 = "1659"
    _1660 = "1660"
    _1661 = "1661"
    _1662 = "1662"
    _1663 = "1663"
    _1664 = "1664"
    _1665 = "1665"
    _1666 = "1666"
    _1667 = "1667"
    _1668 = "1668"
    _1669 = "1669"
    _1670 = "1670"
    _1671 = "1671"
    _1672 = "1672"
    _1800 = "1800"
    _1801 = "1801"
    _1802 = "1802"
    _1803 = "1803"
    _1804 = "1804"
    _1805 = "1805"
    _1806 = "1806"
    _1900 = "1900"
    _1901 = "1901"
    _1902 = "1902"
    _1903 = "1903"
    _1904 = "1904"
    _1905 = "1905"
    _1906 = "1906"
    _1907 = "1907"
    _1908 = "1908"
    _1910 = "1910"
    _1911 = "1911"
    _1912 = "1912"
    _1913 = "1913"
    _1914 = "1914"
    _2000 = "2000"
    _2001 = "2001"
    _2002 = "2002"
    _2003 = "2003"
    _2004 = "2004"
    _2005 = "2005"
    _2006 = "2006"
    _2007 = "2007"
    _2008 = "2008"
    _2009 = "2009"
    _2010 = "2010"
    _2011 = "2011"
    _2012 = "2012"
    _2013 = "2013"
    _2014 = "2014"
    _2015 = "2015"
    _2016 = "2016"
    _2017 = "2017"
    _2018 = "2018"
    _2019 = "2019"
    _2020 = "2020"
    _2021 = "2021"
    _2022 = "2022"
    _2023 = "2023"
    _2024 = "2024"
    _2025 = "2025"
    _2026 = "2026"
    _2027 = "2027"
    _2028 = "2028"
    _2029 = "2029"
    _2030 = "2030"
    _2031 = "2031"
    _2032 = "2032"
    _2033 = "2033"
    _2034 = "2034"
    _2035 = "2035"
    _2036 = "2036"
    _2037 = "2037"
    _2038 = "2038"
    _2039 = "2039"
    _2040 = "2040"
    _2041 = "2041"
    _2042 = "2042"
    _2043 = "2043"
    _2044 = "2044"
    _2045 = "2045"
    _2046 = "2046"
    _2100 = "2100"
    _2101 = "2101"
    _2102 = "2102"
    _2103 = "2103"
    _2104 = "2104"
    _2105 = "2105"
    _2106 = "2106"
    _2107 = "2107"
    _2108 = "2108"
    _2109 = "2109"
    _2110 = "2110"
    _2111 = "2111"
    _2112 = "2112"
    _2113 = "2113"
    _2114 = "2114"
    _2115 = "2115"
    _2200 = "2200"
    _2201 = "2201"
    _2202 = "2202"
    _2203 = "2203"
    _2204 = "2204"
    _2205 = "2205"
    _2206 = "2206"
    _2207 = "2207"
    _2300 = "2300"
    _2500 = "2500"
    _2501 = "2501"
    _2502 = "2502"
    _2600 = "2600"
    _2601 = "2601"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        
    }

    attribute_map = {
        
    }

    def __init__(self):
        """
        ExceptionsPlatformErrorCodes - a model defined in Swagger
        """



    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ExceptionsPlatformErrorCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
