# OpenSimulationInterface.CSharp

This repository contains the build pipeline to generate C# code for the OpenSimulationInterface (OSI) protocol buffers. 
The generated code is packaged as a NuGet package `OpenSimulationInterface.CSharp` and published on NuGet.

## Building the Project

To build the project, follow these steps:

Open the project on visual studio and build the project.
Make sure to have python 3 installed on your machine.

The necessary build steps are defined within the *.csproj file and will do:
1. Install the required version dependencies by running the setup script.
   ```sh
   python setup.py
   ```

2. Generate the C# files from the `.proto` files.
   ```sh
   protoc --proto_path=%userprofile%\.nuget\packages\google.protobuf.tools\3.26.1\tools --proto_path=open-simulation-interface --csharp_out=.\gen open-simulation-interface\*.proto
   ```

3. Compile the code.

## Usage

After installing the `OpenSimulationInterface.CSharp` package, you can use the generated classes in your C# projects. Here is an example:


```csharp
using Osi3;
using Google.Protobuf;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Create an instance of GroundTruth and initialize properties
        var groundTruth = new GroundTruth
        {
            Version = new InterfaceVersion { Major = 3, Minor = 7, Patch = 0 },
            Timestamp = new Timestamp { Seconds = 1234567890, Nanos = 123456789 },
            HostVehicleId = new Identifier { Id = 1 },
            // Add other properties as needed
        };

        // Serialize to binary
        byte[] data = groundTruth.ToByteArray();
        Console.WriteLine($"Serialized GroundTruth to {data.Length} bytes.");

        // Deserialize from binary
        var deserializedGroundTruth = GroundTruth.Parser.ParseFrom(data);
        Console.WriteLine($"Deserialized GroundTruth with version {deserializedGroundTruth.Version.Major}.{deserializedGroundTruth.Version.Minor}.{deserializedGroundTruth.Version.Patch}.");
    }
}
```
