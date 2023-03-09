//#include <opencv2/opencv.hpp>
#include <string> // for std::string
using std::string;

// Working
string getFilename(const string& filepath) {
    for (int i = filepath.size() - 1; i >= 0; i--) {
        if (filepath[i] == '/') {
            string filename = "";
            for (int j = 1; j < filepath.size()-i; j++) {
                filename += filepath[j + i];
            }
            return filename;
        }
    }
    return "";
}

/*
// Returns a string (maybe slow? Don't return entire filepath maybe).
string png_to_grayscale(const string& filepath)
{
    string filename = getFilename(filepath);
    
    // Load the PNG image
    cv::Mat image = cv::imread(filepath, cv::IMREAD_UNCHANGED);

    // Convert the image to grayscale
    cv::Mat grayImage;
    cv::cvtColor(image, grayImage, cv::COLOR_RGB2GRAY);

    // Normalize the grayscale image to the range [0, 1]
    grayImage.convertTo(grayImage, CV_32F, 1.0 / 255.0);

    // Save the grayscale image as a PNG file
    cv::imwrite("gray_image.png", grayImage);

    return 0;
}*/