'''
Browser history analysis
'''
def sites_on_date(visits: list, date: str)->set:
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> sites_on_date([('https://youtube.com/', 'YouTube', '2023-10-23', \
'11:55:31.705320', 0),('https://www.youtube.com/', 'YouTube', '2023-10-22', \
'11:55:31.705320', 1083473)],'2023-10-22')
    {'https://www.youtube.com/'}
    """
    output_set=set()
    for i in visits:
        if i[2]==date:
            output_set.add(i[0])
    return output_set
def most_frequent_sites(visits: list, number: int)->set:
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> most_frequent_sites([('https://youtube.com/', 'YouTube', '2023-10-23', \
'11:55:31.705320', 0),('https://youtube.com/', 'YouTube', '2023-10-22', \
'11:55:31.705320', 1083473),('https://www.instagram.com/', 'Instagram', '2023-10-23', \
'11:55:39.190008', 467439),('https://cms.ucu.edu.ua/my/index.php', 'Dashboard', \
'2023-10-23', '11:56:03.912323', 0),('https://www.instagram.com/', 'Instagram', \
'2023-10-23', '11:55:39.655687', 414254256),('https://youtube.com/', 'YouTube', \
'2023-10-22', '11:55:34.348591', 1006174780)],10)=={'https://www.instagram.com/', \
'https://youtube.com/', 'https://cms.ucu.edu.ua/my/index.php'}
    True
    
    """
    compare_dict={}
    output_set=set()
    for i in visits:
        compare_dict.setdefault(i[0],[]).append('1')
    sorted_dick = ' '.join(sorted(compare_dict, key=lambda key: len(compare_dict[key])))
    sorted_dick=sorted_dick.split()
    try:
        for i in range(number):
            output_set.add(sorted_dick[i*-1])
    except IndexError:
        length=len(sorted_dick)
        for i in range (length):
            output_set.add(sorted_dick[i*-1])
    return output_set
def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)

    """
    count, av_list, last_date = 0, [], '0'
    for i in visits:
        if url in i:
            count += 1
            title = i[1]
            av_list.append(i[4])
            last_date = max(last_date, i[2])

    if count == 0:
        return ('', '', '', 0, 0)

    av_res = 0
    for i in av_list:
        av_res += int(i)
    av_res /= count

    lst_to_check = [i[3] for i in visits if i[2] == last_date and url in i]
    time_last = max(lst_to_check)

    return title, last_date, time_last, count, av_res


if __name__=='__main__':
    import doctest
    print(doctest.testmod())
