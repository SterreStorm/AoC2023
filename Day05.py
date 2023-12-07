import time

start_time = time.time_ns()
def parse_input(filename):
    dict_fields = {}
    with open(filename) as file:
        fields = file.read().split('\n\n')
        for i, field in enumerate(fields):
            field = field.split("\n")
            field_number = i
            fieldmaps = []
            for i in range(1, len(field)):
                tempmap = field[i].split(" ")
                tempmap = [int(i) for i in tempmap if i != ""]
                fieldmaps.append(tempmap)
            dict_fields[field_number] = fieldmaps
    return dict_fields


# convert the field maps to a sorted list of data with the conversion delta as well
def convert_fields_to_ranges(fields):
    new_conversion_lists = {}
    for i in range(1, len(fields)):
        conversion_ranges = fields[i]
        new_conversion_ranges = []
        for conversion_range in conversion_ranges:
            dest_start = conversion_range[0]
            source_start = conversion_range[1]
            source_end = source_start + conversion_range[2] - 1
            conversion_delta = dest_start - source_start
            new_conversion_range = [source_start, source_end, conversion_delta]
            new_conversion_ranges.append(new_conversion_range)
        new_conversion_ranges.sort()
        new_conversion_lists[i] = new_conversion_ranges
    return new_conversion_lists

def source_to_dest(working_list, conversion_lists):
    new_working_list = []
    min_all = conversion_lists[0][0]
    max_all = conversion_lists[-1][1]
    for source in working_list:
        for conversion_list in conversion_lists:
            min_list = conversion_list[0]
            max_list= conversion_list[1]
            delta = conversion_list[2]
            if max_list >= source >= min_list:
                destination = source + delta
                new_working_list.append(destination)
                break
            elif min_all > source or source > max_all:
                    new_working_list.append(source)
                    break
            else:
                continue
    return new_working_list


def seeds_to_ranges(seeds):
    list_of_ranges = []
    doubles = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
    for numberset in doubles:
        start = numberset[0]
        end = start + numberset[1] - 1
        newrange = [start, end]
        list_of_ranges.append(newrange)
    return list_of_ranges


def convert_range(starting_range, conversion_lists):
    new_ranges = []
    # starting range working values
    max_range = conversion_lists[-1][1]
    min_range = conversion_lists[0][0]
    new_working_ranges = [starting_range]
   
    for conversion_list in conversion_lists:
        working_ranges = new_working_ranges
        new_working_ranges = []
        for w_range in working_ranges: 
            lower_range= w_range[0]
            upper_range = w_range[1]
            # list values
            min_list = conversion_list[0]
            max_list = conversion_list[1]
            # new values
            delta = conversion_list[2]
            new_lower_range = lower_range + delta
            new_upper_range = upper_range + delta
            new_min_list = min_list + delta
            new_max_list = max_list + delta

            if upper_range <= max_list and lower_range >= min_list:
                new_ranges.append([new_lower_range, new_upper_range])

            elif lower_range < min_list <= upper_range <= max_list:
                new_ranges.append([new_min_list, new_upper_range])
                new_working_ranges.append([lower_range, (min_list - 1)])

            elif min_list <= lower_range <= max_list < upper_range:
                new_ranges.append([new_lower_range, new_max_list])
                new_working_ranges.append([(max_list + 1), upper_range])

            elif lower_range < min_list and max_list < upper_range:
                new_ranges.append([new_min_list, new_max_list])
                new_working_ranges.append([(max_list + 1), upper_range])
                new_working_ranges.append([lower_range, (min_list - 1)])
            else:
                new_working_ranges.append(w_range)
    if len(new_working_ranges) != 0: new_ranges += new_working_ranges

    # print(new_working_ranges,new_ranges)
    return new_ranges


def main(filename):
    fields = parse_input(filename)
    conversion_dict = convert_fields_to_ranges(fields)
    seeds_list = fields[0][0]
    initial_seeds_ranges = seeds_to_ranges(seeds_list)
    final_location_ranges = []
    # part 1
    for conversion_lists in conversion_dict.values():
        seeds_list = source_to_dest(seeds_list, conversion_lists)
    seeds_list.sort()
    
    # print("lowest part 1: " + str(seeds_list[0]))

    # part 2:
    for seeds_range in initial_seeds_ranges: # all initial pairs
        new_working_seeds_ranges = [seeds_range]
        for conversion_lists in conversion_dict.values(): # convert fist pair
            working_seeds_ranges = new_working_seeds_ranges
            new_working_seeds_ranges = []
            for working_range in working_seeds_ranges:
                tmp = convert_range(working_range, conversion_lists)
                new_working_seeds_ranges += tmp
        final_location_ranges += new_working_seeds_ranges


    # print(final_location_ranges)
    final_location_ranges.sort()
    print("lowest part 2: " + str(final_location_ranges[0][0]))


main("input/day05.txt")

print("day 05")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
