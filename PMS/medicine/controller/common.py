class Common:

    def percentageCalculation(total, detect):
        try:
            print(total, detect)
            if total != 0:
                if detect == None:
                    detect = 0
                result = ((int(total) - int(detect))/int(total)) * 100
                return round(result)
            return 0

        except Exception as e:
            print(e)
            return 0