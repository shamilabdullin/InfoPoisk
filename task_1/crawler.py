import shutil

import requests

from bs4 import BeautifulSoup

links = [
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B1%D0%B5%D0%B3_%D0%B8%D0%B7_%D0%A8%D0%BE%D1%83%D1%88%D0%B5%D0%BD%D0%BA%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D1%91%D1%81%D1%82%D0%BD%D1%8B%D0%B9_%D0%BE%D1%82%D0%B5%D1%86_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D1%91%D1%81%D1%82%D0%BD%D1%8B%D0%B9_%D0%BE%D1%82%D0%B5%D1%86_2",
 "https://ru.wikipedia.org/wiki/%D0%A2%D1%91%D0%BC%D0%BD%D1%8B%D0%B9_%D1%80%D1%8B%D1%86%D0%B0%D1%80%D1%8C",
 "https://ru.wikipedia.org/wiki/12_%D1%80%D0%B0%D0%B7%D0%B3%D0%BD%D0%B5%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1957)",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%A8%D0%B8%D0%BD%D0%B4%D0%BB%D0%B5%D1%80%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%92%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D0%BB%D0%B8%D0%BD_%D0%BA%D0%BE%D0%BB%D0%B5%D1%86:_%D0%92%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BA%D0%BE%D1%80%D0%BE%D0%BB%D1%8F",
 "https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B8%D0%BC%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D1%87%D1%82%D0%B8%D0%B2%D0%BE",
 "https://ru.wikipedia.org/wiki/%D0%A5%D0%BE%D1%80%D0%BE%D1%88%D0%B8%D0%B9,_%D0%BF%D0%BB%D0%BE%D1%85%D0%BE%D0%B9,_%D0%B7%D0%BB%D0%BE%D0%B9",
 "https://ru.wikipedia.org/wiki/%D0%92%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D0%BB%D0%B8%D0%BD_%D0%BA%D0%BE%D0%BB%D0%B5%D1%86:_%D0%91%D1%80%D0%B0%D1%82%D1%81%D1%82%D0%B2%D0%BE_%D0%9A%D0%BE%D0%BB%D1%8C%D1%86%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D0%B9%D1%86%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BB%D1%83%D0%B1_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D1%80%D0%B5%D1%81%D1%82_%D0%93%D0%B0%D0%BC%D0%BF",
 "https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D0%BE_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2010)",
 "https://ru.wikipedia.org/wiki/%D0%92%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D0%BB%D0%B8%D0%BD_%D0%BA%D0%BE%D0%BB%D0%B5%D1%86:_%D0%94%D0%B2%D0%B5_%D0%BA%D1%80%D0%B5%D0%BF%D0%BE%D1%81%D1%82%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D1%8B%D0%B5_%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B._%D0%AD%D0%BF%D0%B8%D0%B7%D0%BE%D0%B4_V:_%D0%98%D0%BC%D0%BF%D0%B5%D1%80%D0%B8%D1%8F_%D0%BD%D0%B0%D0%BD%D0%BE%D1%81%D0%B8%D1%82_%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%BD%D1%8B%D0%B9_%D1%83%D0%B4%D0%B0%D1%80",
 "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5_%D0%BF%D0%B0%D1%80%D0%BD%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%BB%D0%B5%D1%82%D0%B0%D1%8F_%D0%BD%D0%B0%D0%B4_%D0%B3%D0%BD%D0%B5%D0%B7%D0%B4%D0%BE%D0%BC_%D0%BA%D1%83%D0%BA%D1%83%D1%88%D0%BA%D0%B8_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D1%8C_%D1%81%D0%B0%D0%BC%D1%83%D1%80%D0%B0%D0%B5%D0%B2",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D1%8C_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%B8%D0%B5_%D1%8F%D0%B3%D0%BD%D1%8F%D1%82_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4_%D0%91%D0%BE%D0%B3%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%96%D0%B8%D0%B7%D0%BD%D1%8C_%D0%BF%D1%80%D0%B5%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1997)",
 "https://ru.wikipedia.org/wiki/%D0%AD%D1%82%D0%B0_%D0%BF%D1%80%D0%B5%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F_%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C",
 "https://ru.wikipedia.org/wiki/%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D1%8B%D0%B5_%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B._%D0%AD%D0%BF%D0%B8%D0%B7%D0%BE%D0%B4_IV:_%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BD%D0%B0%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B0%D1%81%D1%82%D0%B8_%D1%80%D1%8F%D0%B4%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE_%D0%A0%D0%B0%D0%B9%D0%B0%D0%BD%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B8%D0%BB%D1%8F_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A3%D0%BD%D0%B5%D1%81%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%80%D0%B8%D0%B7%D1%80%D0%B0%D0%BA%D0%B0%D0%BC%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%81%D1%82%D0%B5%D0%BB%D0%BB%D0%B0%D1%80",
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%B7%D0%B8%D1%82%D1%8B_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D0%BE%D0%BD_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A5%D0%B0%D1%80%D0%B0%D0%BA%D0%B8%D1%80%D0%B8_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1962)",
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B4%D0%BE%D0%B7%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%BB%D0%B8%D1%86%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C_%D0%9B%D0%B5%D0%B2",
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D0%B0%D0%BD%D0%B8%D1%81%D1%82_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80_2:_%D0%A1%D1%83%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B4%D0%B5%D0%BD%D1%8C",
 "https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B7%D0%B0%D0%B4_%D0%B2_%D0%B1%D1%83%D0%B4%D1%83%D1%89%D0%B5%D0%B5_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%98%D0%BA%D1%81",
 "https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D1%8B%D0%B5_%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1936)"
 "https://ru.wikipedia.org/wiki/%D0%93%D0%BB%D0%B0%D0%B4%D0%B8%D0%B0%D1%82%D0%BE%D1%80_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2000)",
 "https://ru.wikipedia.org/wiki/%D0%9F%D1%81%D0%B8%D1%85%D0%BE",
 "https://ru.wikipedia.org/wiki/%D0%9E%D1%82%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%B8%D0%BA%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%9E%D0%B3%D0%BD%D0%B8_%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B3%D0%BE_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0",
 "https://ru.wikipedia.org/wiki/1%2B1_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9E%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2014)",
 "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%B3%D0%B8%D0%BB%D0%B0_%D1%81%D0%B2%D0%B5%D1%82%D0%BB%D1%8F%D1%87%D0%BA%D0%BE%D0%B2",
 "https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%B6_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9E%D0%B4%D0%BD%D0%B0%D0%B6%D0%B4%D1%8B_%D0%BD%D0%B0_%D0%94%D0%B8%D0%BA%D0%BE%D0%BC_%D0%97%D0%B0%D0%BF%D0%B0%D0%B4%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%81%D0%B0%D0%B1%D0%BB%D0%B0%D0%BD%D0%BA%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BA%D0%B8%D0%BD%D0%BE%D1%82%D0%B5%D0%B0%D1%82%D1%80_%C2%AB%D0%9F%D0%B0%D1%80%D0%B0%D0%B4%D0%B8%D0%B7%D0%BE%C2%BB",
 "https://ru.wikipedia.org/wiki/%D0%9E%D0%BA%D0%BD%D0%BE_%D0%B2%D0%BE_%D0%B4%D0%B2%D0%BE%D1%80",
 "https://ru.wikipedia.org/wiki/%D0%A7%D1%83%D0%B6%D0%BE%D0%B9_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%90%D0%BF%D0%BE%D0%BA%D0%B0%D0%BB%D0%B8%D0%BF%D1%81%D0%B8%D1%81_%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F",
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BC%D0%BD%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D0%B4%D0%B8%D0%BA%D1%82%D0%B0%D1%82%D0%BE%D1%80",
 "https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B8%D0%B0%D0%BD%D0%B0_%D0%94%D0%B6%D0%BE%D0%BD%D1%81:_%D0%92_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0%D1%85_%D1%83%D1%82%D1%80%D0%B0%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BA%D0%BE%D0%B2%D1%87%D0%B5%D0%B3%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%94%D0%B6%D0%B0%D0%BD%D0%B3%D0%BE_%D0%BE%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B6%D0%B4%D1%91%D0%BD%D0%BD%D1%8B%D0%B9",
 "https://ru.wikipedia.org/wiki/%D0%96%D0%B8%D0%B7%D0%BD%D1%8C_%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D1%85",
 "https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%BE%D0%BB%D0%B5%D1%82%D0%BD%D0%B8%D0%B9_%D1%81%D1%82%D0%B0%D1%80%D0%B8%D0%BA,_%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9_%D0%B2%D1%8B%D0%BB%D0%B5%D0%B7_%D0%B2_%D0%BE%D0%BA%D0%BD%D0%BE_%D0%B8_%D0%B8%D1%81%D1%87%D0%B5%D0%B7",
 "https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%BE%D0%BF%D1%8B_%D1%81%D0%BB%D0%B0%D0%B2%D1%8B",
 "https://ru.wikipedia.org/wiki/%D0%94%D0%B6%D0%BE%D0%BA%D0%B5%D1%80_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2019)",
 "https://ru.wikipedia.org/wiki/%D0%92%D0%90%D0%9B%D0%9B-%D0%98",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9C%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D0%B8:_%D0%92%D0%BE%D0%B9%D0%BD%D0%B0_%D0%B1%D0%B5%D1%81%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%91%D1%83%D0%BB%D1%8C%D0%B2%D0%B0%D1%80_%D0%A1%D0%B0%D0%BD%D1%81%D0%B5%D1%82_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%B8%D0%B4%D0%B5%D1%82%D0%B5%D0%BB%D1%8C_%D0%BE%D0%B1%D0%B2%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F",
 "https://ru.wikipedia.org/wiki/%D0%9E%D0%BB%D0%B4%D0%B1%D0%BE%D0%B9_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2003)",
 "https://ru.wikipedia.org/wiki/%D0%A7%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA-%D0%BF%D0%B0%D1%83%D0%BA:_%D0%A7%D0%B5%D1%80%D0%B5%D0%B7_%D0%B2%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B5%D1%81%D1%81%D0%B0_%D0%9C%D0%BE%D0%BD%D0%BE%D0%BD%D0%BE%D0%BA%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BA%D1%82%D0%BE%D1%80_%D0%A1%D1%82%D1%80%D0%B5%D0%B9%D0%BD%D0%B4%D0%B6%D0%BB%D0%B0%D0%B2,_%D0%B8%D0%BB%D0%B8_%D0%9A%D0%B0%D0%BA_%D1%8F_%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%82%D0%B0%D0%BB_%D0%B1%D0%BE%D1%8F%D1%82%D1%8C%D1%81%D1%8F_%D0%B8_%D0%BF%D0%BE%D0%BB%D1%8E%D0%B1%D0%B8%D0%BB_%D0%B1%D0%BE%D0%BC%D0%B1%D1%83",
 "https://ru.wikipedia.org/wiki/%D0%A2%D1%91%D0%BC%D0%BD%D1%8B%D0%B9_%D1%80%D1%8B%D1%86%D0%B0%D1%80%D1%8C:_%D0%92%D0%BE%D0%B7%D1%80%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BB%D0%B5%D0%B3%D0%B5%D0%BD%D0%B4%D1%8B",
 "https://ru.wikipedia.org/wiki/%D0%9E%D0%B4%D0%BD%D0%B0%D0%B6%D0%B4%D1%8B_%D0%B2_%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%A2%D0%B2%D0%BE%D1%91_%D0%B8%D0%BC%D1%8F",
 "https://ru.wikipedia.org/wiki/%D0%A7%D1%83%D0%B6%D0%B8%D0%B5_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1986)",
 "https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B9%D0%BD%D0%B0_%D0%9A%D0%BE%D0%BA%D0%BE",
 "https://ru.wikipedia.org/wiki/%D0%9C%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D0%B8:_%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB",
 "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BF%D0%B5%D1%80%D0%BD%D0%B0%D1%83%D0%BC_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B0%D1%81%D0%BE%D1%82%D0%B0_%D0%BF%D0%BE-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%A5%D1%80%D0%B0%D0%B1%D1%80%D0%BE%D0%B5_%D1%81%D0%B5%D1%80%D0%B4%D1%86%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B9_%D0%B8_%D0%B0%D0%B4",
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B4%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F_%D0%BB%D0%BE%D0%B4%D0%BA%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%B8%D0%B3%D1%80%D1%83%D1%88%D0%B5%D0%BA",
 "https://ru.wikipedia.org/wiki/3_%D0%B8%D0%B4%D0%B8%D0%BE%D1%82%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%B0%D0%B4%D0%B5%D0%B9_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D1%81%D1%81%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5_%D1%83%D0%B1%D0%BB%D1%8E%D0%B4%D0%BA%D0%B8",
 "https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BD%D0%B8%D1%86%D0%B0_%D0%A3%D0%B8%D0%BB%D0%BB_%D0%A5%D0%B0%D0%BD%D1%82%D0%B8%D0%BD%D0%B3",
 "https://ru.wikipedia.org/wiki/%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D1%8B%D0%B5_%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B._%D0%AD%D0%BF%D0%B8%D0%B7%D0%BE%D0%B4_VI:_%D0%92%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B4%D0%B6%D0%B5%D0%B4%D0%B0%D1%8F",
 "https://ru.wikipedia.org/wiki/%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D0%BE%D1%87%D0%BA%D0%B8_%D0%BD%D0%B0_%D0%B7%D0%B5%D0%BC%D0%BB%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D1%88%D0%B5%D0%BD%D1%8B%D0%B5_%D0%BF%D1%81%D1%8B",
 "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B4%D0%B8%D1%81%D1%81%D0%B5%D1%8F_2001_%D0%B3%D0%BE%D0%B4%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%BA%D0%B2%D0%B8%D0%B5%D0%BC_%D0%BF%D0%BE_%D0%BC%D0%B5%D1%87%D1%82%D0%B5",
 "https://ru.wikipedia.org/wiki/%D0%9E%D1%85%D0%BE%D1%82%D0%B0_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_2012)",
 "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC)",
 "https://ru.wikipedia.org/wiki/%D0%9C_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1931)",
 "https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%87%D0%BD%D0%BE%D0%B5_%D1%81%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5_%D1%87%D0%B8%D1%81%D1%82%D0%BE%D0%B3%D0%BE_%D1%80%D0%B0%D0%B7%D1%83%D0%BC%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B6%D0%B4%D0%B0%D0%BD%D0%B8%D0%BD_%D0%9A%D0%B5%D0%B9%D0%BD",
 "https://ru.wikipedia.org/wiki/%D0%94%D0%B0%D0%BD%D0%B3%D0%B0%D0%BB",
 "https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D0%B3%D0%B0_%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B5%D0%B4%D0%BB%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%B8_%D0%97%D0%B0%D0%BA%D0%B0_%D0%A1%D0%BD%D0%B0%D0%B9%D0%B4%D0%B5%D1%80%D0%B0",
 "https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%8E%D1%89%D0%B8%D0%B5_%D0%BF%D0%BE%D0%B4_%D0%B4%D0%BE%D0%B6%D0%B4%D1%91%D0%BC",
 "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BB%D1%8B%D1%88_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC,_1921)"
]

def main():
    i = 1
    index = open("index.txt", "w", encoding="utf-8")

    # проходимся по всему массиву ссылок
    for link in links:
        print(f"Парсим {i}-ую страницу")
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        site = open(f"sites/{i}.html", "w", encoding="utf-8")   # f"sites/{i}.txt"

        site_body = soup.find('div', {"class": "mw-body-content"}).get_text(separator=" ").strip()

        # записываем контент нашей статьи
        site.write(f"{site_body}")
        site.close()
        index.write(f"{i} {link}\n")
        i += 1

    index.close()
    shutil.make_archive("выкачка", 'zip', "sites")


main()
