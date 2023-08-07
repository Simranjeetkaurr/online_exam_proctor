course = Course(course_category=category, course_name=name, course_description=description)
        if image:
            course.course_image = image
        else:
        # Set the default image file if no image is provided
            default_image_path = './frontend/media/course_images/courses.gif'
        with open(default_image_path, 'rb') as f:
            course.course_image = ImageFile(f)
        
        course.save()