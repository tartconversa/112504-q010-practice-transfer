# 急救公益课程的技能保持与补训

仅记录公益课程和模拟演练，无真实个人信息。日期使用当地业务日。技能映射的状态适用于相应演练版本。

## 资料

CSV 样例为合成记录，使用 UTF-8，首行为字段名。多值用竖线分隔，空单元格表示来源未填。记录日期和业务生效日期各有含义。

- skills.csv 的字段为 version、station、outcome、basis、comparable。
- cohorts.csv 的字段为 person、cohort、tower、shift、joined、course、version。
- observations.csv 的字段为 attempt、person、station、at、kind、score、received。
- invitations.csv 的字段为 invite、person、round、day、outcome、probability。
- shifts.csv 的字段为 person、tower、level、shift、start、stop。
- refreshers.csv 的字段为 slot、tower、shift、date、station、instructor、capacity、state。

## 运行资料检查

在项目根目录使用 Python 3.11 或更高版本。依赖仅为标准库。

~~~sh
python3 -m compileall -q tests
python3 -m unittest discover -s tests -v
~~~
