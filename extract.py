  #!/usr/bin/env python3                                                                                                                                                                               
  """Extract a page range from a PDF file.
                                                                                                                                                                                                       
  Usage: pdf-extract <input.pdf> <output.pdf> <start_page>-<end_page>
  Example: pdf-extract "Math Book.pdf" output.pdf 9-15
  """

  import sys

  from pypdf import PdfReader, PdfWriter


  def main():
      if len(sys.argv) != 4:
          print("Usage: pdf-extract <input.pdf> <output.pdf> <start>-<end>")
          print("Example: pdf-extract input.pdf output.pdf 9-15")
          sys.exit(1)

      input_path = sys.argv[1]
      output_path = sys.argv[2]
      page_range = sys.argv[3]

      try:
          start_str, end_str = page_range.split("-")
          start = int(start_str)
          end = int(end_str)
      except ValueError:
          print(f"Error: invalid page range '{page_range}'. Use format: 9-15")
          sys.exit(1)

      try:
          reader = PdfReader(input_path)
      except FileNotFoundError:
          print(f"Error: file not found: {input_path}")
          sys.exit(1)

      total = len(reader.pages)

      if start < 1 or end > total or start > end:
          print(f"Error: page range {start}-{end} is out of bounds (PDF has {total} pages)")
          sys.exit(1)

      writer = PdfWriter()
      for i in range(start - 1, end):
          writer.add_page(reader.pages[i])

      with open(output_path, "wb") as f:
          writer.write(f)

      print(f"Extracted pages {start}-{end} from '{input_path}' -> '{output_path}'")


  if __name__ == "__main__":
      main()
