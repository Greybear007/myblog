from django.db import models


from DjangoUeditor.models import UEditorField

# Create your models here.
class  Category(models.Model):
	"""
	定义分类
	"""


	STATUS_NORMAL = 1
	STATUS_DELETE = 0
	STATUS_ITEMS = (
		(STATUS_NORMAL, "正常"),
		(STATUS_DELETE, "删除"),
	)
	name = models.CharField(max_length=128, verbose_name="名称")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = "分类"

class Tag(models.Model):
	"""
	定义分类
	"""


	STATUS_NORMAL = 1
	STATUS_DELETE = 2
	STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
	)

	name = models.CharField(max_length=128, verbose_name="名称")
	status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = "标签"




class Artical(models.Model):
    """定义文章"""


    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
    	( STATUS_NORMAL, "正常"),
        ( STATUS_DELETE, "删除"),
        ( STATUS_DRAFT, "草稿"),
    )
    title = models.CharField(max_length=128, verbose_name="标题")
    descrition = models.CharField(max_length=1024, verbose_name="简介")
    content = UEditorField(
    	width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",
    	upload_settings={"imageMaxSize":1204000000},
    	verbose_name='内容'
    )

    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	#updated_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(Tag, verbose_name="标签" )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ["-id"]
			
		