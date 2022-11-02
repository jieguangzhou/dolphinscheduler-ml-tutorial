from pydolphinscheduler.core.process_definition import ProcessDefinition
from pydolphinscheduler.tasks.python import Python
from pydolphinscheduler.tasks.shell import Shell

download_dir = "/tmp/demo"
store_dir = "dolphinscheduler"
download_link = "https://github.com/apache/dolphinscheduler/archive/refs/heads/dev.zip"
file_name = download_link.split("/")[-1]


def largest_size():
    from pathlib import Path

    download_dir = "/tmp/demo"
    store_dir = "dolphinscheduler"

    result = (None, 0)
    paths = Path(download_dir).joinpath(store_dir).glob("**/*")

    for path in paths:
        # skip is path is directory
        if path.is_dir():
            continue
        file_size = path.stat().st_size
        if result[0] is None or file_size > result[1]:
            result = (path.name, file_size)
    print(result)


def most_frequently():
    from pathlib import Path

    download_dir = "/tmp/demo"
    store_dir = "dolphinscheduler"

    ext_cnt = {}
    paths = Path(download_dir).joinpath(store_dir).glob("**/*")

    for path in paths:
        # skip is path is directory
        if path.is_dir():
            continue
        ext = path.suffix
        ext_cnt[ext] = ext_cnt[ext] + 1 if ext in ext_cnt else 1
    print(max(ext_cnt.items(), key=lambda p: p[1]))


with ProcessDefinition(
        name="top_ten_size_files",
        tenant="zhongjiajie",
) as pd:
    prepare = Shell(
        name="prepare_dir",
        command=f"mkdir -p {download_dir}; rm -rf {download_dir}/*"
    )

    download = Shell(
        name="download_resources",
        command=f"wget -P {download_dir} {download_link}"
    )

    compress = Shell(
        name="compress_tar",
        command=f"cd {download_dir}; unzip {file_name} -d {store_dir}"
    )

    largest_file = Python(
        name="largest_file",
        definition=largest_size,
    )

    most_type = Python(
        name="most_type",
        definition=most_frequently,
    )

    prepare >> download >> compress >> [
        largest_file,
        most_type,
    ]

    pd.run()
