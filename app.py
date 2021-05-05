# -*- coding: utf-8 -*-

import sys
from data import Data, Color
from os.path import expanduser

__version__ = "1.0.0"

_options = {
    "vendor_code": None,
    "gender": None,
    "short": False,
    "verbose": False,
    "case": False,
    "version": False,
    "help": False
}
def getGenderStr(num):
    if num == 1:
        return Color.BG_CYAN + Color.BOLD + Color.WHITE + " ♂ " + Color.END
    elif num == 2:
        return Color.BG_PURPLE + Color.BOLD + Color.WHITE + " ♀ " + Color.END
    elif num == 0:
        return Color.BG_YELLOW + Color.BOLD + Color.WHITE + " ? " + Color.END
    else:
        return Color.BG_RED + Color.BOLD + Color.WHITE + " - " + Color.END
def searchInObject(query, data) :
    for value in [query == data["Name"], query in data["Name"], query == data["Code"]] if _options["case"] else [query == data["Name"], query.lower() in data["Name"].lower(), query.lower() == data["Code"]]:
        if value:
            return True
    return False
def getPairs(code):
    for pairsVal in Data["Pairs"]:
        if pairsVal["Code"] == code:
            return pairsVal
def printVocal(vocal, short = False, verbose = False):
    result = Color.BOLD + vocal["Name"] + Color.END + (" [" + vocal["Code"] + "]" if verbose else "") + " " + getGenderStr(vocal["Gender"])

    if not short:
        pair = "Not a pair"
        if vocal["Pair"] == None:
            products = vocal["Products"]
        else:
            pair_ = getPairs(vocal["Pair"])
            pair = pair_["Name"]
            products = pair_["Products"]
            del pair_

        if len(products) == 1:
            result += "\n" + "- Product:"
        else:
            result += "\n" + "- Products:"

        for productsVal in products:
            result += "\n" + "    " + productsVal["Name"]

            for engineVal in Data["Engine"]:
                if engineVal["Code"] == productsVal["Engine"]:
                    for vendorsVal in Data["Vendors"]:
                        if vendorsVal["Code"] == engineVal["Vendor"]:
                            result += "\n" + "      Engine: " + engineVal["Name"] + (" [" + engineVal["Code"] + "]" if verbose else "") + " (" + vendorsVal["Name"] + ")"
                            break

            if len(productsVal["Vendors"]) == 1:
                result += "\n" + "      Vendor: "
            else:
                result += "\n" + "      Vendors: "

            _productVendors = []
            for vendorsVal in Data["Vendors"]:
                if vendorsVal["Code"] in productsVal["Vendors"]:
                    if "Companies" in vendorsVal and verbose:
                        _companiesList = []
                        for companiesVal in vendorsVal["Companies"]:
                            _companiesList.append(companiesVal["Name"] + " (" + companiesVal["Country"] + ")")
                        _companies = " by (" + ", ".join(_companiesList) + ")"
                    else:
                        _companies = ""
                    _productVendors.append(vendorsVal["Name"] + (" [" + vendorsVal["Code"] + "]" if verbose else "") + " (" + vendorsVal["Country"] + ")" + _companies)
            result += ", ".join(_productVendors)
            del _productVendors

            if len(productsVal["Languages"]) == 1:
                result += "\n" + "      Language: " + productsVal["Languages"][0]
            else:
                result += "\n" + "      Languages: " + ", ".join(productsVal["Languages"])

            result += "\n" + "      Voice: " + ("Unpublished" if productsVal["Voice"] == None else productsVal["Voice"])

            if productsVal["Date"] == None:
                result += "\n" + "      Release Date: Unknown"
            else:
                result += "\n" + "      Release Date: " + productsVal["Date"]
        result += "\n" + "- Pair:"
        result += "\n" + "    " + pair
    return result
def printPairs(group, short = False, verbose = False):
    result = []
    for singersVal in Data["Singers"]:
        if singersVal["Pair"] == group["Code"]:
            result.append(printVocal(singersVal, short, verbose))
    return result
def main():
    if len(sys.argv) == 1:
        sys.argv.append("help")

    command = ""
    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            if arg.startswith("--vendor="):
                input_ = arg.replace("--vendor=", "")
                for value in Data["Vendors"]:
                    if searchInObject(input_, value):
                        _options["vendor_code"] = value["Code"]
            elif arg.startswith("--gender="):
                input_ = arg.replace("--gender=", "").lower()
                if input_ in ["0", "1", "2"]:
                    _options["gender"] = int(input_)
                elif input_ in ["unknown", "male", "female"]:
                    _options["gender"] = {"unknown": 0, "male": 1, "female": 2}[input_]
                else:
                    print("Please specify the gender.")
                    sys.exit(1)
            elif arg == "--short":
                _options["short"] = True
            elif arg == "--verbose":
                _options["verbose"] = True
            elif arg == "--match-case":
                _options["case"] = True
            elif arg == "--help":
                _options["help"] = True
            elif arg == "--version":
                _options["version"] = True
            else:
                print("Unknown argument: " + arg)
                sys.exit(1)
        elif arg.startswith("-"):
            for value in arg[1:]:
                if value == "s":
                    _options["short"] = True
                elif value == "v":
                    _options["verbose"] = True
                elif value == "c":
                    _options["case"] = True
                elif value == "i":
                    _options["verbose"] = True
                else:
                    print("Unknown argument: " + value + " in " + arg)
                    sys.exit(1)
        else:
            if command == "":
                command = arg
            else:
                print("Invalid argument: " + arg)
                sys.exit(1)
    if command == "help": _options["help"] = True
    if command == "version": _options["version"] = True

    if _options["help"]:
        print("Vocautils " + __version__ + " | Data set version " + str(Data["Version"]) + " (" + Data["Update-Date"] + ")")
        print("Commands:")
        print("  voca [Query]           : Search a singer.")
        print("  voca singers           : Show all singers.")
        print("  voca vendors           : Show all vendors.")
        print("  voca version           : Show the version number.")
        print("  voca help              : Show the help.")
        print("Options:")
        print("  --vendor=[Vendor Name] : Narrow down a vendor.")
        print("  --gender=[Gender]      : Narrow down a gender. (Unknown, Male or Female)")
        print("  --short or -s          : Shorten the message.")
        print("  --match-case or -c     : Match case.")
        print("  --verbose or -v        : Show detailed information.")
    elif _options["version"]:
        print("Vocautils " + __version__ + " | Data set version " + str(Data["Version"]) + " (" + Data["Update-Date"] + ")")
    elif command == "singers":
        result = []
        for value in Data["Singers"]:
            if _options["vendor_code"] != None and _options["gender"] != None:
                if _options["vendor_code"] in value["Vendors"] and _options["gender"] == value["Gender"]:
                    result.append(printVocal(value, _options["short"], _options["verbose"]))
            elif _options["vendor_code"] != None:
                if _options["vendor_code"] in value["Vendors"]:
                    result.append(printVocal(value, _options["short"], _options["verbose"]))
            elif _options["gender"] != None:
                if _options["gender"] == value["Gender"]:
                    result.append(printVocal(value, _options["short"], _options["verbose"]))
            else:
                result.append(printVocal(value, _options["short"], _options["verbose"]))
        if result:
            print("\n".join(result))
            sys.exit(0)
        else:
            print("No matches found.")
            sys.exit(1)
    elif command == "vendors":
        result = []
        for value in Data["Vendors"]:
            result.append(value["Name"] + ("" if _options["short"] else (" [" + value["Code"] + "]" if _options["verbose"] else "") + " (" + value["Country"] + ")"))
        if result:
            print("\n".join(result))
            sys.exit(0)
        else:
            print("No matches found.")
            sys.exit(1)
    else:
        result = []
        for value in Data["Singers"]:
            if searchInObject(command, value):
                valueVendors = []
                for productsVal in (getPairs(value["Pair"]) if value["Pair"] != None else value)["Products"]:
                    valueVendors += productsVal["Vendors"]
                if _options["vendor_code"] != None and _options["gender"] != None:
                    if _options["vendor_code"] in valueVendors and _options["gender"] == value["Gender"]:
                        result.append(printVocal(value, _options["short"], _options["verbose"]))
                elif _options["vendor_code"] != None:
                    if _options["vendor_code"] in valueVendors:
                        result.append(printVocal(value, _options["short"], _options["verbose"]))
                elif _options["gender"] != None:
                    if _options["gender"] == value["Gender"]:
                        result.append(printVocal(value, _options["short"], _options["verbose"]))
                else:
                    result.append(printVocal(value, _options["short"], _options["verbose"]))
        if not result:
            for value in Data["Pairs"]:
                if searchInObject(command, value):
                    result += printPairs(value, _options["short"], _options["verbose"])
        result = list(dict.fromkeys(result))

        if result:
            print(("\n" if _options["short"] else "\n\n").join(result))
            sys.exit(0)
        else:
            print("No matches found.")
            sys.exit(1)
if __name__ == '__main__':
    main()
