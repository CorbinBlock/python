import unzip_files
import zip_files

def service_func():
    print('compress and decompress service test (.zip format)')

if __name__ == '__main__':
    # zip_service.py executed as script
    # do something
    service_func()
    unzip_files.unzip_func("Zip_time_series.csv.zip", r"C:\Users\Corbin\ssd")
